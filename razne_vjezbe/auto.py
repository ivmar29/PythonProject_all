class Auto:
    def __init__(self, marka, model, gorivo=10):
        self.marka = marka
        self.model = model
        self.gorivo = gorivo
    #Metode
    def vozi(self, km):
        potrosnja = km * 0.1
        if potrosnja > self.gorivo:
            print("Nema dovoljno goriva za tu vožnju!")
        else:
            self.gorivo -= potrosnja
            print(f"Auto je prešao {km} km. Preostalo goriva: {self.gorivo:.2f} L.")

    def natoci(self, litara):
        if self.gorivo + litara >= 55:
            self.gorivo = 55
            print("Rezervoar je pun (55 L).")
        else:
            self.gorivo += litara
            print(f"Natočeno {litara} L. Trenutno stanje: {self.gorivo:.2f} L.")

    def __str__(self):
        return f"Auto {self.marka} {self.model} ima {self.gorivo:.2f} L goriva."
# Objekt
# Test
auto1 = Auto("Nissan", "Skyline", 15)
print(auto1)

auto1.vozi(50)
auto1.natoci(20)
auto1.natoci(80)
print(auto1)