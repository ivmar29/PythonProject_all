from knjiznica import Knjiznica
from clan import Clan
from knjiga import Knjiga
knjiga = None
clan = None

#stvorimo knjiznicu
knjiznica = Knjiznica("Gradska knjiznica")

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
    knjiznica.dodaj_knjigu(knjiga)
#kreiraj clanovee
elif a == "2":
    print("=== Unos novog člana ===")
    clan = Clan(input("Ime: "), input("Godine: "), input("Email: "))
    knjiznica.dodaj_clana(clan)
# posudi knjigu
elif a == "3":
    print("=== Posuđivanje knjiga ===")
    ime_clan= input("Ime člana: ")
    naslov_knjiga = input("Unesite ime knjige: ")
    knjiznica.posudi_knjigu(ime_clan, naslov_knjiga)
# vrati knjigu
elif a == "4":
    print("=== Vrati knjigu ===")
    ime_clan = input("Ime člana: ")
    naslov_knjiga = input("Unesite ime knjige: ")
    knjiznica.vrati_knjigu(ime_clan, naslov_knjiga)


