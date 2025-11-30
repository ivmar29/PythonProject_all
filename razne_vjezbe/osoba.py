class Osoba:
    #Konstuktor definira sto svaka osoba ima
    def __init__(self, ime, godine):
        self.ime = ime
        self.godine = godine

    #Metoda koja ispisuje predstavljanje
    def predstavi_se(self):
        print(f"Bok ja sam {self.ime} i imam {self.godine} godina.")

# Kreirajmo objekte (instance klase)
osoba1 = Osoba("Ivan", 31)
osoba2 = Osoba("Matea", 29)

#Poziv metode za svaku osobu
osoba1.predstavi_se()
osoba2.predstavi_se()