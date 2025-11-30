recenica = input("Unesite željenu rečenicu: ")
recenica = recenica.lower()

brojanje = {}

for slovo in recenica:
    if slovo.isalpha():
        if slovo in brojanje:
            brojanje[slovo] += 1
        else:
            brojanje[slovo] = 1

for slovo, broj in brojanje.items():
    print(f"{slovo} : {broj}")