from knjiznica import Knjiznica
from clan import Clan
from knjiga import Knjiga


#kreiranje knjigea
knjiga1 = Knjiga("Star Wars 1", "Lucas")
knjiga2 = Knjiga("Star Wars 2", "Lucas")
knjiga3 = Knjiga("Star Wars 3", "Lucas")
knjiga4 = Knjiga("Star Wars 4", "Lucas")

#kreiraj clanovee
clan1 = Clan(1,"Ivan",31, "ivan@gmail.com",)
clan2 = Clan(2,"Matea",29, "matea@gmail.com",)
clan3 = Clan(3,"Valentina",22, "tina@gmail.com",)
clan4 = Clan(4,"Dubravka",51, "dubi@gmail.com",)

#stvorimo knjiznicu
knjiznica = Knjiznica("Gradska knjiznica")

#dodaj knjigu
knjiznica.dodaj_knjigu(knjiga1)
knjiznica.dodaj_knjigu(knjiga2)


#dodaje clanove
knjiznica.dodaj_clana(clan1)
knjiznica.dodaj_clana(clan2)




