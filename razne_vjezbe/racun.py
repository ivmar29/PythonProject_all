class Racun:
    def __init__(self, vlasnik, stanje=0):
        self.vlasnik = vlasnik
        self.stanje = stanje

    def uplata(self, iznos):
        self.stanje += iznos
        print(f"Uplaćeno {iznos} EUR. Novo stanje: {self.stanje} EUR.")

    def isplata(self, iznos):
        if iznos <= self.stanje:
            self.stanje -= iznos
            print(f"Isplaćeno {iznos} EUR. Novo stanje: {self.stanje} EUR.")
        else:
            print("Nemate dovoljno sredstava za isplatu.")

    def __str__(self):
        return f"Račun vlasnika {self.vlasnik}, trenutno stanje: {self.stanje} EUR"

# Test
racun1 = Racun("Ana", 100)
print(racun1)

racun1.uplata(50)
racun1.isplata(30)
racun1.isplata(200)

