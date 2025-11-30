class Knjiznica:
    def __init__(self,naziv):
        self.naziv = naziv
        self.knjige = []
        self.clanovi = []

    def dodaj_knjigu(self,knjiga):
        self.knjige.append(knjiga)
        print(f"Knjiga '{knjiga.naslov_knjige}' je dodana u knjižnicu '{self.naziv}'")

    def dodaj_clana(self,clan):
        self.clanovi.append(clan)
        print(f"Član '{clan.ime_clana}' dodan u knjiznicu '{self.naziv}'")

    def prikazi_knjige(self):
        print(f"\n Popis knjiga u '{self.naziv}':")
        for knjiga in self.knjige:
            status = "Dostupna" if knjiga.dostupno else "Posuđena"
            print(f"- {knjiga.naslov_knjige} ({knjiga.autor}) - {status}")

    def posudi_knjigu(self,ime_clana,naslov_knjige):
        #pronađi člana
        clan = next((c for c in self.clanovi if c.ime_clana == ime_clana), None)
        #pronađi knjigu
        knjiga= next ((k for k in self.knjige if k.naslov_knjige == naslov_knjige), None)

        if not clan:
            print(f"Ćlan '{ime_clana}' nije pronađen.")
            return

        if not knjiga:
            print(f"Knjiga '{naslov_knjige}' nije pronađena.")
            return

        if knjiga.dostupno:
            knjiga.dostupno = False
            clan.posudene_knjige.append(knjiga)
            print(f"{ime_clana} je posudio '{naslov_knjige}'")
        else:
            print(f"Knjiga '{naslov_knjige}' je već posuđena.'")

    def vrati_knjigu(self,ime_clana,naslov_knjige):
        clan = next((c for c in self.clanovi if c.ime_clana == ime_clana), None)
        if not clan:
            print(f"Član '{ime_clana}' nije pronađen")
            return

        knjiga = next((k for k in clan.posudene_knjige if k.naslov_knjige == naslov_knjige), None)
        if not knjiga:
            print(f"{ime_clana}' nema knjigu '{naslov_knjige}'.")
            return

        knjiga.dostupno = True
        clan.posudene_knjige.remove(knjiga)
        print(f"{ime_clana} je vratio '{naslov_knjige}'")

class Knjiga:
    def __init__(self,naslov_knjige,autor):
        self.naslov_knjige = naslov_knjige
        self.autor = autor
        self.dostupno = True

class Clan:
    def __init__(self,ime_clana):
        self.ime_clana = ime_clana
        self.posudene_knjige = []


# def posuditi(self,knjiga):
#       if knjiga.dostupno:
#           knjiga.dostupno = False
#           self.posudene_knjige.append(knjiga)
#           print(f"{self.ime} je posudio '{knjiga.naslov}'.")
#       else:
#           print(f"'{knjiga.naslov}' knjiga je posuđena.")

#   def vratiti(self,knjiga):
#       if knjiga in self.posudene_knjige:
#           knjiga.dostupno = True
#           self.posudene_knjige.remove(knjiga)
#           print(f"{self.ime} je vratio '{knjiga.naslov}'.")
#       else:
#           print(f"{self.ime} nema tu knjigu.")

#Test

# Kreiranje objekata
k1 = Knjiga("1984", "George Orwell")
k2 = Knjiga("Na Drini ćuprija", "Ivo Andrić")
k3 = Knjiga("Gospodar prstenova - Prstenova družina", "J.R.R. Tolkien")
k4 = Knjiga("Gospodar prstenova - Dvije kule", "J.R.R. Tolkien")
k5 = Knjiga("Gospodar prstenova - Povratak kralja", "J.R.R. Tolkien")

ana = Clan("Ana")
ivan = Clan("Ivan")

knjiznica = Knjiznica("Gradska knjižnica")
knjiznica.dodaj_knjigu(k1)
knjiznica.dodaj_knjigu(k2)
knjiznica.dodaj_knjigu(k3)
knjiznica.dodaj_clana(ana)
knjiznica.dodaj_clana(ivan)



knjiznica.posudi_knjigu("Ana","1984")
knjiznica.posudi_knjigu("Ivan","Na Drini ćuprija")
knjiznica.vrati_knjigu("Ana","1984")
knjiznica.prikazi_knjige()