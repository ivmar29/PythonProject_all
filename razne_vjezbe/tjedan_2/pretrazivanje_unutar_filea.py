import pandas as pd

# učitaj datoteku
df = pd.read_csv("adresar.csv", header=None, names=["Ime", "Broj", "Email"])

# unos korisnika
pretraga = input("Unesite ime ili email za pretragu: ")

# filtriranje pomoću pandas funkcije .str.contains()
rezultat = df[df["Ime"].str.contains(pretraga, case=False) | df["Email"].str.contains(pretraga, case=False)]

print(rezultat)