import json
import os
class Knjiznica:
    def __init__(self,name,json_file = "knjiznica.json"):
        self.name = name
        self.knjige = [] # Svaka knjižnica će imati svoju listu knjiga (početno praznu).
        self.clanovi = []
        self.json_file = json_file # Pamti ime JSON fajla gdje će se čuvati podaci o knjigama.

        # ----------------------------------------------------
        # Učitavanje JSON-a ako postoji
        # ----------------------------------------------------

        if os.path.exists(json_file):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)  # pokušaj učitati JSON
            except (json.JSONDecodeError, FileNotFoundError):
                data = {}  # ako je prazan ili oštećen
        else:
            data = {}  # ako ne postoji

        self.knjige = data.get("knjige", [])
        #Pokušaj dohvatiti vrijednost pod ključem "knjige", Ako taj ključ ne postoji (ili JSON nema "knjige"), vrati praznu listu []
        self.clanovi = data.get("clanovi", [])
        # Isto.

        # Garantira da self.knjige i self.clanovi uvijek postoje kao liste
        # Sprječava greške kada pokušamo kasnije dodati knjigu ili člana u listu
        #------------------------------------------------------------------------------------------------

    def __str__(self): # definiranje načina na koji će se objekt te klase prikazati kao tekst.
        return f"{self.name}"

    def spremi_u_json(self):
        data = {
            "knjige":self.knjige,
            "clanovi":self.clanovi,
         }
        with open(self.json_file,"w", encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)

    def dodaj_knjigu(self, knjiga):
        # Provjera praznih unosa
        if not knjiga.name.strip() or not knjiga.author.strip(): # "" u pythonu znaci "false"
            print("Niste unijeli naziv knjige i/ili autora!")
            return
        # Provjera duplikata
        for k in self.knjige:
            if k["name"].lower() == knjiga.name.lower() and k["author"].lower() == knjiga.author.lower():
                print(f"Knjiga '{knjiga.name}' već postoji!")
                return  # izlaz, ne dodajemo duplikat
        # Unos knjige
        self.knjige.append({
            "name": knjiga.name,
            "author": knjiga.author
        })
        self.spremi_u_json()  #odmah spremi novu listu u json
        print(f"Knjiga '{knjiga.name}' dodana u knjižnicu '{self.name}'.")

    def dodaj_clana(self,clan):

        # Provjera praznih unosa
        if not clan.name.strip()  or not clan.age.strip() or not clan.email.strip(): # "" u pythonu znaci "false"
            print("Niste unijeli sve podatke!")
            return

        # Provjera jesu li godine broj
        if not clan.age.isdigit():
            print("Niste unijeli broj kao godine!")
            return

        # Provjera duplikata
        for k in self.clanovi:
            if k["email"] == clan.email:
                print(f"Član '{clan.name}' već postoji!")
                return  # izlaz, ne dodajemo duplikat
        # auto ID
        clan.id = len(self.clanovi) + 1

        # Dodavanje u listu
        self.clanovi.append({
            "id": clan.id,
            "name": clan.name,
            "age": clan.age,
            "email": clan.email
        })
        # Spremanje u JSON
        self.spremi_u_json()  # odmah spremi novu listu u json
        print(f"Član '{clan.name}' je dodan/a.")

   # def posudi_knjigu(self, knjiga):

   # def vrati_knjigu(self,knjiga):

