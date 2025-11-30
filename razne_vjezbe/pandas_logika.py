import pandas
import pandas as pd

###print(df)### -  ispisuje nepotpuni data frame(prvih 5 i zadnji 5 redova)
###orint(df.to_string())### - ispisuje sve u terminal


# Series
#
# Jednodimenzionalni niz podataka (kao napredna lista ili 1 kolona iz DataFrame-a).
#
# Ima vrijednosti i indeks.
#
# Sadrži samo jedan stupac podataka.
#-----------------------------------------------------------------------------------
#DataFrame

#Dvodimenzionalna tabela podataka (redovi × kolone).

#Sastoji se od više Series objekata spojenih zajedno.

#Ima indeks redova i nazive kolona.
#------------------------------------------------------------------------------------
#pristupanje odrešenom podatku mozemo raditi pomoci iloc i loc.
#.loc - Koristi nazive redova i kolona (indeks labela), ne numeričke pozicije.
# npr   df.loc['A', 'ime']        # red 'A', kolona 'ime'
#       df.loc['A':'C', 'ime']    # uključuje i 'C'
#       df.loc[:, ['ime', 'godine']]
#--------------------------------------------------------------------
# Filtriranje
# df = pd.read_csv('pokemon.csv')
# tall_pokemon = df[df['Height'] >= 2]
# print(tall_pokemon)
#--------------------------------------------------------------------
# Aggregate funcions - služe za sažimanje podataka — uzimaju više vrijednosti i vraćaju jednu (npr. sumu, prosjek, minimum…).
# | Funkcija    | Objašnjenje           |
# | ----------- | --------------------- |
# | `sum()`     | zbir                  |
# | `mean()`    | prosjek               |
# | `median()`  | medijana              |
# | `min()`     | minimum               |
# | `max()`     | maksimum              |
# | `count()`   | broj elemenata        |
# | `nunique()` | broj jedinstvenih     |
# | `std()`     | standardna devijacija |
# | `var()`     | varijansa             |
# primjeri

# Whole dataframe
#     print(df.mean(numeric_only=True))
#     print(df.sum(numeric_only=True))
#     print(df.min(numeric_only=True))
#     print(df.max(numeric_only=True))
#     print(df.count())

# Single column
#     print(df["Height"].mean())
#     print(df["Height"].sum())
#     print(df["Height"].min())
#     print(df["Height"].max())
#     print(df["Height"].count())

# groupby():
#
# Podijeli DataFrame na grupe (npr. po koloni "grad")
#
# Obradi svaku grupu (npr. izračunaj sumu prodaje u svakom gradu)
#
# Spoji rezultate u novi DataFrame
#
# Zbog toga se često kaže da radi:
#
# ➤ Split — Apply — Combine
#
# (podijeli — primijeni — spoji)

# primjer

# group = groupby("Type1")
#
# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())
#-------------------------------------------------------------------------------------------
# # DATA CLEANING - the process of fixing/removing:
#                 - incomplete, incorrect or irrelevant data.
#                 - 75% of work done with Pandas is data cleaning.

# # 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

# # 2.Handle missing data
#     df = dropna(subset=["Type2"]) - "drop not available" -izbacit ce sve redove koji ne posjeduju nikakvu vrijednost tipa "NaN"
#     df = fillna({"Type2":"None"}) - "fill any not available values" popunjava sve podatke koji ne posjeduju vrijednos s "None"
#
# # 3.Fix inconsitent value
#     df["Type1"] = df["Type1"].replace({"Grass":"GRASS"}) - mjenja vrijednosti iz stupca "Type1" npr. u sva velika slova za odabranu vrijednost
#
# # 4. Standardize text
#     df["Name"] = df["Name"].str.lower() - mijenja cijeli stupac u mala slova
#
# # 5. Fix data types
#     df["Legendary"] = df["Legendary"].astype(bool) - promjena vijednosti koju ima red iz 0 i 1 u boolena
#-----------------------------------------------------------------------------------------------------------------
# PROGRAM 1

#i.loc - indeksiranje po numeričkim pozicijama (0,1,2)

#data = [100, 200, 300]

#series = pd.Series(data, index = ["a", "b", "c"])

#series.loc["c"] = 500

#print(series)

# Program 2

# data = {
#    "Name": ["Spužvabob", "Patrik", "Karamarko"],
#     "Age": ["30", "35","50"]
# }
#
# df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])
#
# # Add new column
# df["Job"] = ["Cook", "N/A", "Cashier"]
#
# # Add new row
#
# new_row = pd.DataFrame([{"Name": "Sandy", "Age": "32", "Job": "Engineer"}],
#                             index = ["Employee 4"])
#
# df = pd.concat([df, new_row])  # pd.concat je funkcija u pandas biblioteci koja služi za spajanje (konkatenaciju) više Series ili DataFrame objekata u jedan.
#
# print(df)

