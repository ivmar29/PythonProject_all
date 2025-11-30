print("Ovo je mini kviz od 3 pitanja!")
odgovor_a = int(input("Krenimo s 1. pitanjem: Koje godine je počelo 21. stoljeće?: "))
brojac_odgovora = 0
if odgovor_a == 2001:
    print("Točan odgovor. Idemo dalje!")
    brojac_odgovora += 1
else:
    print("Odgovor je netočan. Nastavimo.")

odgovor_b = int(input("Nastavimo s 2. pitanjem: Koliko je planeta u Sunčevom sustavu?: "))
if odgovor_b == 8:
    print("Točan odgovor. Idemo dalje!")
    brojac_odgovora += 1
else:
    print("Odgovor je netočan. Nastavimo.")

odgovor_c = input("Zadnje (3.) pitanje: 'Ti si meni sin, ja ti nisam otac'. Tko sam ti ja?: ").lower()
if odgovor_c == "majka" or odgovor_c == "mama":
    print("Točan odgovor.")
    brojac_odgovora += 1
else:
    print("Odgovor je netočan.")

print(f"Ukupan rezultat: {brojac_odgovora}/3")


