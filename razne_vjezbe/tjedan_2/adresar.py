#ime, broj, email
import pandas as pd
df = pd.read_csv("adresar.csv",header = None, names = ["Ime", "Broj", "Email"])
print(df)

ime = input("Unesite ime: ")
broj = input("Unesite broj: ")
email = input("Unesite email: ")

with open("adresar.csv", "a",encoding="utf-8") as file:
    file.write(f"{ime},{broj},{email}\n")
df = pd.read_csv("adresar.csv",header = None, names = ["Ime", "Broj", "Email"])
print(df)