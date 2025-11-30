#Program koji broji rijeci i ispusje 5 najcescih
import re
with open("example.txt", "r",encoding="utf-8") as file:
    content = file.read() #čita content
    content = content.lower() #sve prebacuje u lowercase

# Podijeli tekst u riječi po razmacima
rijeci = re.findall(r'\b\w+\b', content)  # pronalazi samo riječi (slova i brojeve)----uklanja znakove tipa ".",",","!","?"

brojanje = {}
for rijec in rijeci: #za svaku rijec u grupi rijeci
    if rijec.isalpha(): #The isalpha() method returns True if all the characters are alphabet letters (a-z).
        if rijec in brojanje: # Ukoliko se rijeci nalazi u rijecniku povecaj kolicinu za 1
            brojanje[rijec] += 1
        else:
            brojanje[rijec] = 1 # Ukoliko se rijeci ne nalazi u rijecniku dodaj ju i daj joj vrijednost 1

sortirano = sorted(brojanje.items(), key=lambda item: item[1], reverse=True) #Sortira ih po velicini od veceg prema manjem

# ispiši samo prvih 5
for kljuc, vrijednost in sortirano[:5]:
    print(f"{kljuc} = {vrijednost}")