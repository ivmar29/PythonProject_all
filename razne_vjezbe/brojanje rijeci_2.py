#Napravi program koji ucita tekst i ispise koliko se puta koja rijec koristila.
#Ignoriraj velika i mala slova

text = "Mara ima malo janje, takozvano Mara janje"
broj_rijeci = {}

for rijec in text.lower().split(): #.split dopusta prolazenje po rijecima ne po znakovima(bez.split() varijabla "text" je lista znakova, a s njom je lista rijeci
        broj_rijeci[rijec] = broj_rijeci.get(rijec, 0) + 1 #dict.get(key, default) metoda pokušava dobiti vrijednost za ključ.
                                                           #Ako ključ postoji, vraća njegovu vrijednost.
                                                           #Ako ključ ne postoji, vraća default vrijednost, ovdje 0.
                                                           # +1 Ako rijec postoji povecava vrijednost za 1, a ako ne postoji povecava default vrijednost za 1 (0+1)=1

print(broj_rijeci)