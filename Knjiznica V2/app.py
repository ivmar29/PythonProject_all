from knjiznica import Knjiznica
from clan import Clan
from knjiga import Knjiga
knjiga = None
clan = None
# Izbornik
print("=== IZBORNIK ===")
print("Izaberite broj")
a = input("1. Dodaj knjigu\n"
          "2. Dodaj člana\n"
          "3. Posudi knjigu\n"
          "4. Vrati knjigu\n")

#kreiranje knjige
if a == "1":
    print("=== Unos nove knjige ===")
    knjiga = Knjiga(input("Unesi naziv knjige: "),input("Unesi naziv autora: "))
#kreiraj clanovee
elif a == "2":
    print("=== Unos novog člana ===")
    clan = Clan(input("Ime: "), input("Godine: "), input("Email: "))


#stvorimo knjiznicu
knjiznica = Knjiznica("Gradska knjiznica")

#dodaj knjigu
if knjiga is not None: #ukoliko smo odabrali opciju koja nije "dodaj knjigu"
    # ovo sprijecava da knjiznica doda knjigu a ne postoji ta varijabla "knjiga". Početna vriijednost knjige gore u programu je None.
    knjiznica.dodaj_knjigu(knjiga)


#dodaje clanove
if clan is not None:
    knjiznica.dodaj_clana(clan)




