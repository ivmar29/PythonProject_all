import json
import os
class Knjiznica:
    def __init__(self,name,json_file = "knjiznica.json"):
        self.name = name
        self.knjige = [] # Svaka knjižnica će imati svoju listu knjiga (početno praznu).
        self.clanovi = []
        self.json_file = json_file # Pamti ime JSON fajla gdje će se čuvati podaci o knjigama.

        #ako json postoji ucitaj podatke
        if os.path.exists(json_file):
            try:
                with open(json_file,"r", encoding="utf-8") as f:
                    content = f.read().strip() # Ove dvije linije otvaraju JSON fajl i učitavaju njegov sadržaj kao tekst,
                                               # bez nepotrebnih razmaka, kako bi se moglo provjeriti je li datoteka prazna.

                # ako je fajl prazan, napravi praznu listu
                #ovo radimo zato što json.load(f) NE MOŽE učitati prazan fajl i baca grešku
                if content == "":
                    self.knjige = []
                else:
                    self.knjige = json.loads(content)

            except json.JSONDecodeError:
            # fajl postoji, ali je oštećen
                self.knjige = []

        else:
            #ako ne postji napravi prazni json
            self.knjige = []
            with open(self.json_file,"w", encoding="utf-8") as f:
                json.dump(self.knjige, f,index=4,ensure_ascii=False)

    def __str__(self):
        return f"{self.name}"

    def spremi_u_json(self):
        with open(self.json_file,"w", encoding="utf-8") as f:
            json.dump(self.knjige, f, indent=4,ensure_ascii=False)

    def dodaj_knjigu(self, knjiga):
        self.knjige.append({
            "name": knjiga.name,
            "author": knjiga.author
        })
        #odmah spremi novu listu u json
        self.spremi_u_json()
        print(f"Knjiga '{knjiga.name}' dodana u knjižnicu '{self.name}'.")

    def dodaj_clana(self,clan):
        self.knjige.append(clan)
        print(f"Član '{clan.name}' je dodan/a.")

   # def posudi_knjigu(self, knjiga):

   # def vrati_knjigu(self,knjiga):

