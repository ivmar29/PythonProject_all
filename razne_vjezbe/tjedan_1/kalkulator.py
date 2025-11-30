a = int(input("Molimo unesite 1. broj: "))
b = int(input("Molimo unesite 2. broj: "))

x = input("Odaber radnju: 1. Zbrajanje, 2.Oduzimanje, 3. Množenje, 4. Dijeljenje :")

if x == "1":
    print(a+b)
elif x == "2":
    print(a-b)
elif x == "3":
    print(a*b)
elif x == "4":
    if b == 0:
        print("Greška: ne može se dijeliti s nulom!")
    else:
        print(round(a / b, 2))
else:
    print("Nepoznata operacija! Molimo odaberite 1, 2, 3 ili 4.")




