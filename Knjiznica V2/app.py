from knjiznica import Knjiznica
from clan import Clan
from knjiga import Knjiga


#kreiranje knjige
knjiga1 = Knjiga("Star Wars 1", "Lucas")
knjiga2 = Knjiga("Star Wars 2", "Lucas")
knjiga3 = Knjiga("Star Wars 3", "Lucas")
knjiga4 = Knjiga("Star Wars 4", "Lucas")

#kreiraj clanove
clan1 = Clan("Ivan",31, "ivan@gmail.com",)
clan2 = Clan("Matea",29, "matea@gmail.com",)
clan3 = Clan("Valentina",22, "tina@gmail.com",)
clan4 = Clan("Dubravka",51, "dubi@gmail.com",)

#stvorimo knjiznicu
knjiznica = Knjiznica("Gradska knjiznica")

#dodaj knjigu
knjiznica.dodaj_knjigu(knjiga1)
knjiznica.dodaj_knjigu(knjiga2)
knjiznica.dodaj_knjigu(knjiga3)
knjiznica.dodaj_knjigu(knjiga4)

#dodaje clanove
knjiznica.dodaj_clana(clan1)
knjiznica.dodaj_clana(clan2)
knjiznica.dodaj_clana(clan3)
knjiznica.dodaj_clana(clan4)



