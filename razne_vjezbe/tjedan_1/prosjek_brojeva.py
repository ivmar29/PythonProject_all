lista_brojeva = [1,2,3,4,5,6,7,8,9,12,14,15,28,36,42,43,55,57,86,98,99,100]
ukupno_brojeva = len(lista_brojeva)
zbroj_liste = sum(lista_brojeva)

prosjek_brojeva =round(zbroj_liste/ukupno_brojeva,3)

print(f"Prosjek brojeva u listi je: {prosjek_brojeva}")