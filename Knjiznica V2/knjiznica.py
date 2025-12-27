import json
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

    def dodaj_knjigu(self, knjiga):
        if not knjiga.name.strip() or not knjiga.author.strip():
            return False # GUI ce prikazati poruku

        for k in self.knjige:
            if k.name.lower() == knjiga.name.lower() and k.author.lower() == knjiga.author.lower():
                return False

        self.knjige.append(knjiga)
        self.spremi_u_json()
        print(f"Knjiga '{knjiga.name}' dodana u knjižnicu '{self.name}'.")
        return True

    def dodaj_clana(self,clan):

        if not clan.name.strip() or not clan.age.strip() or not clan.email.strip(): #Nisu svi podaci uneseni
            return False

        if not clan.age.isdigit():#Godine nisu broj
            return False

        for c in self.clanovi: #Duplikat clanova
            if c.email == clan.email:
                return False

        clan.id = len(self.clanovi) + 1
        self.clanovi.append(clan)
        self.spremi_u_json()
        print(f"Član '{clan.name}' je dodan/a.")
        return True

    def posudi_knjigu(self, ime_clana, naslov_knjige):
        clan = next((c for c in self.clanovi if c.name.lower() == ime_clana.lower()), None)
        knjiga = next((k for k in self.knjige if k.name.lower() == naslov_knjige.lower()), None)

        if not clan:
            print(f"Član '{ime_clana}' nije pronađen")
            return False

        if not knjiga:
            print(f"Knjiga '{naslov_knjige}' nije pronađena.")
            return False

        if not knjiga.dostupno:
            print(f"Knjiga '{knjiga.name}' trenutno nije dostupna.")
            return False

        knjiga.dostupno = False
        clan.posudene_knjige.append(knjiga.name)
        self.spremi_u_json()
        return True



    def vrati_knjigu(self, ime_clana, naslov_knjige):
        clan = next((c for c in self.clanovi if c.name.lower() == ime_clana.lower()), None)
        knjiga = next((k for k in self.knjige if k.name.lower() == naslov_knjige.lower()), None)

        if not clan:
            print(f"Član '{ime_clana}' nije pronađen")
            return False

        if not knjiga:
            print(f"Knjiga '{naslov_knjige}' nije pronađena.")
            return False

        knjiga.dostupno = True
        clan.posudene_knjige.remove(knjiga.name)
        self.spremi_u_json()
        return True



