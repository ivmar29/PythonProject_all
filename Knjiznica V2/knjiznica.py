import json
import re
import os
from knjiga import Knjiga
from clan import Clan
class Knjiznica:
    def __init__(self,name,json_file = "knjiznica.json"):
        self.name = name
        self.knjige = [] # Svaka knjižnica će imati svoju listu knjiga (početno praznu).
        self.clanovi = []
        self.json_file = json_file # Pamti ime JSON fajla gdje će se čuvati podaci o knjigama.

        self.ucitaj_iz_jsona()

    def __str__(self):
        return self.name
        # ----------------------------------------------------
        # Učitavanje i spremanje
        # ----------------------------------------------------
    def ucitaj_iz_jsona(self):
        if not os.path.exists(self.json_file):
            return
        try:
            with open(self.json_file, "r", encoding="utf-8") as f:
                data = json.load(f)  # pokušaj učitati JSON
        except json.JSONDecodeError:
            return
        # KNJIGE
        self.knjige = [
            Knjiga(
                k["name"],
                k["author"],
                k.get("dostupno", True)
            )
            for k in data.get("knjige", [])
        ]

        # ČLANOVI
        self.clanovi = []
        for c in data.get("clanovi", []):
            clan = Clan(
                c["name"],
                c["age"],
                c["email"],
                c.get("id")
            )
            clan.posudene_knjige = c.get("posudene_knjige", [])
            self.clanovi.append(clan)


    def spremi_u_json(self):
        data = {
            "knjige": [
                {
                    "name": k.name,
                    "author": k.author,
                    "dostupno": k.dostupno,
                }
                for k in self.knjige
            ],
            "clanovi": [
                {
                    "id": c.id,
                    "name": c.name,
                    "age": c.age,
                    "email": c.email,
                    "posudene_knjige": c.posudene_knjige,
                }
                for c in self.clanovi
            ],
        }

        with open(self.json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    @staticmethod
    def normaliziraj(naziv):
        return naziv.replace(" ", "").lower()  # uklanja razmake i pretvara u mala slova
    @staticmethod
    def email_ok(email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    def dodaj_knjigu(self, knjiga):
        if not knjiga.name.strip() or not knjiga.author.strip():#Provjerava je li barem jedno polje prazno (naziv knjige ili autor).
            return False, "Niste unjeli naziv knjige i/ili autora"  # GUI ce prikazati poruku             #Ako jest, odmah vraća False jer nema smisla dalje provjeravati.

        for k in self.knjige:
            #Provjerava postoji li već ista knjiga u knjižnici (duplikat).
            if k.name.lower() == knjiga.name.lower() and k.author.lower() == knjiga.author.lower():
                return False, f"Knjiga '{knjiga.name}' već postoji"

        self.knjige.append(knjiga) #Knjiga je dodana u knjiznicu
        self.spremi_u_json()
        return True, f"Knjiga '{knjiga.name}' je dodana u knjižnicu '{self.name}.'"

    def dodaj_clana(self,clan):

        if not clan.name.strip() or not clan.age.strip() or not clan.email.strip(): #Nisu svi podaci uneseni
            return False, "Niste unjeli sve podatke."

        if not clan.age.isdigit():#provjerava da li je string sastavljen samo od brojeva
            return False, "Godine moraj biti broj"

        clan.age = int(clan.age)
        if clan.age < 1 or clan.age > 99:
            return False, "Raspon godina:(1-99)!"

        if not self.email_ok(clan.email):
            return False, "Neispravni format email adrese!"


        # Provjera duplikata preko email-a
        for c in self.clanovi:
            if c.email == clan.email:
                return False, f"Član {clan.name} vec postoji. Pokušajte ponovo. "

        clan.id = len(self.clanovi) + 1
        self.clanovi.append(clan)
        self.spremi_u_json()
        return True, f"Član '{clan.name}' je dodan/a."

    def posudi_knjigu(self, ime_clana, naslov_knjige):
        clan = next((c for c in self.clanovi if self.normaliziraj(c.name) == self.normaliziraj(ime_clana)), None)
        knjiga = next((k for k in self.knjige if self.normaliziraj(k.name) == self.normaliziraj(naslov_knjige)), None)

        if not clan and not knjiga:
            return False, f"Knjiga '{naslov_knjige}' i član '{ime_clana}' nisu pronađeni"

        if not clan:
            return False, f"Član '{ime_clana}' nije pronađen"

        if not knjiga:
            return False, f"Knjiga '{naslov_knjige}' nije pronađena."

        if not knjiga.dostupno:
            return False, f"Knjiga '{knjiga.name}' trenutno nije dostupna."



        knjiga.dostupno = False
        clan.posudene_knjige.append(knjiga.name)
        self.spremi_u_json()
        return True, "Knjiga je uspiješno posuđena!"



    def vrati_knjigu(self, naslov_knjige):
        #pronalazi knjigu i onda ju normalizira(velika/mala slova, razmaci) i uspoređuje s imenom koje je korisnik unjeo.
        knjiga = next((k for k in self.knjige if self.normaliziraj(k.name) == self.normaliziraj(naslov_knjige)), None)

        if not knjiga:
            return False, f"Knjiga '{naslov_knjige}' nije pronađena."

        #pronalazi člana i onda provjerava da li se ime knjige koje je unešeno nalazi u listi posuđenih knjiga tog clana te nastavlja.
        clan = next((c for c in self.clanovi if knjiga.name in c.posudene_knjige), None)

        if not clan:
            return False, f"Knjiga nije posuđena niti jednom članu"

        knjiga.dostupno = True
        clan.posudene_knjige.remove(knjiga.name)
        self.spremi_u_json()

        return True, f"Knjiga '{knjiga.name}' je vraćena"



