import random
attempts = 1
x = int(input("Unesite jedan broj od 1-10: "))
while x < 1 or x > 10:
    print("Krivo!")
    x = int(input("Unesite jedan broj od 1-10: "))

c = random.randint(1,10)
while x != c:
    print("Pokušajte ponovo.")
    x = int(input("Unesite jedan broj od 1-10: "))
    attempts += 1

print(f"Točno! Pogodili ste broj {c} iz {attempts} pokušaja.")
