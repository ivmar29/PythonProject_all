# Ova skripta ce generirati podatke (lazne) o vremenu unutar jedne godine
# Svaki sat mora imati 1 zabiljezene vrijednosti temperature.
# Generirati cemo podatke o temperaturi za početak a kasnije cemo dodati u kolicninu padalina koju cemo generirati u postocima za svaki dan.(Očitava se jednom dnevno na kraju dana.
# Napravi da se generirani podaci spremaju u CSV file, i također da imam opciju u kod kad pokrenemo skriptu da vidimo i u terminalu.

import pandas as pd
import random
import calendar

# godine možemo staviti 2024 kao primjer (prijestupna)
godina = 2024

# svi mjeseci
mjeseci = ["January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December"]

# minimalne i maksimalne temperature po mjesecu
temp_range = {
    "January": (-5, 5),
    "February": (-3, 7),
    "March": (0, 12),
    "April": (5, 18),
    "May": (10, 22),
    "June": (15, 28),
    "July": (18, 35),
    "August": (18, 34),
    "September": (12, 28),
    "October": (7, 20),
    "November": (2, 12),
    "December": (-2, 7)
}

# najviše dana u mjesecu je 31
dani = list(range(1, 32))
df = pd.DataFrame({"day": dani}) #Ova linija koda kreira DataFrame s jednim stupcem "day" koji sadrži brojeve od 1 do 31.

# popuni mjesec po mjesec sa stvarnim brojem dana
for i, mjesec in enumerate(mjeseci, start=1):
    broj_dana = calendar.monthrange(godina, i)[1]  # broj dana u mjesecu
    min_temp, max_temp = temp_range[mjesec]

    # generiraj random temperature za stvarne dane
    vrijednosti = [round(random.uniform(min_temp, max_temp), 1) for _ in range(broj_dana)]

    # dodaj prazne ćelije za dane koji ne postoje
    vrijednosti += [""] * (31 - broj_dana)

    df[mjesec] = vrijednosti

# pregled
print(df)

# spremi u CSV
df.to_csv("vrijeme.csv", index=False, encoding="utf-8")

