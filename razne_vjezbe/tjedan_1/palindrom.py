rijec = input("Unesite riječ: ")
rijec = rijec.lower()

palindrom = True  # pretpostavimo da je riječ palindrom

for i in range(len(rijec) // 2):
    if rijec[i] != rijec[-(i + 1)]:  # uspoređujemo prvi sa zadnjim, drugi sa pretposljednjim itd.
        palindrom = False
        break

if palindrom:
    print(f"Riječ {rijec} je palindrom.")
else:
    print(f"Riječ {rijec} nije palindrom.")



#rijec[-(i + 1)]

#Negativni indeks u Pythonu znači “broji od kraja”:

#-1 → zadnji znak

#-2 → pretposljednji znak

#-3 → treći od kraja

#Dakle, -(i+1) uzima simetričan znak s kraja riječi.