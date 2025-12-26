import customtkinter as ctk
from knjiznica import Knjiznica
from clan import Clan
from knjiga import Knjiga

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Kreiranje glavnog prozora
app = ctk.CTk()

app.title("Knjiznica V2")
app.geometry("700x450")

#stvorimo knjiznicu
knjiznica = Knjiznica("Gradska knjiznica")

# Frame
content_frame = ctk.CTkFrame(app)
content_frame.pack(fill="both", expand=True, pady=20)

# Funkcija za čišćenje ekrana
def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()
# "Dodaj knjigu
def prikazi_dodaj_knjigu():
    clear_frame()

    naslov = ctk.CTkEntry(content_frame, placeholder_text="Naziv knjige")
    naslov.pack(pady=10)

    autor = ctk.CTkEntry(content_frame, placeholder_text="Autor")
    autor.pack(pady=10)

    def spremi():
        knjiga = Knjiga(naslov.get(), autor.get())
        knjiznica.dodaj_knjigu(knjiga)

    spremi_btn = ctk.CTkButton(
        content_frame,
        text="Spremi knjigu",
        command=spremi
    )
    spremi_btn.pack(pady=20)

# "Dodaj člana"
def prikazi_dodaj_clana():
    clear_frame()

    ime = ctk.CTkEntry(content_frame, placeholder_text="Ime")
    ime.pack(pady=5)

    godine = ctk.CTkEntry(content_frame, placeholder_text="Godine")
    godine.pack(pady=5)

    email = ctk.CTkEntry(content_frame, placeholder_text="Email")
    email.pack(pady=5)

    def spremi():
        clan = Clan(ime.get(), godine.get(), email.get())
        knjiznica.dodaj_clana(clan)

    spremi_btn = ctk.CTkButton(
        content_frame,
        text="Spremi člana",
        command=spremi
    )
    spremi_btn.pack(pady=20)

# "Posudi knjigu"
def prikazi_posudi_knjigu():
    clear_frame()

    naslov_knjige = ctk.CTkEntry(content_frame, placeholder_text="Naziv knjige")
    naslov_knjige.pack(pady=10)

    ime_clana = ctk.CTkEntry(content_frame, placeholder_text="Ime člana")
    ime_clana.pack(pady=10)

    def spremi():
        knjiznica.posudi_knjigu(ime_clana.get(),naslov_knjige.get())

    spremi_btn = ctk.CTkButton(
        content_frame,
        text="Posudi knjigu",
        command=spremi
    )
    spremi_btn.pack(pady=20)

# "Vrati knjigu"
def prikazi_vrati_knjigu():
    clear_frame()

    naslov_knjige = ctk.CTkEntry(content_frame, placeholder_text="Naziv knjige")
    naslov_knjige.pack(pady=10)

    ime_clana = ctk.CTkEntry(content_frame, placeholder_text="Ime člana")
    ime_clana.pack(pady=10)

    def spremi():
        knjiznica.vrati_knjigu(ime_clana.get(),naslov_knjige.get())

    spremi_btn = ctk.CTkButton(
        content_frame,
        text="Vrati knjigu",
        command=spremi
    )
    spremi_btn.pack(pady=20)

def izbor_promijenjen(odabir):
    if odabir == "Dodaj knjigu":
        prikazi_dodaj_knjigu()
    elif odabir == "Dodaj Člana":
        prikazi_dodaj_clana()
    elif odabir == "Posudi knjigu":
        prikazi_posudi_knjigu()
    elif odabir == "Vrati knjigu":
        prikazi_vrati_knjigu()


# Opcije
izbor = ["Dodaj knjigu", "Dodaj Člana", "Posudi knjigu", "Vrati knjigu"]

# Create option menu
menu = ctk.CTkOptionMenu(app,values=izbor, command=izbor_promijenjen)
# govori: Prikaži ovaj widget u prozoru. bez pack() ili grid() widget se ne vidi
menu.pack(pady=20)
 # pokrece gui, slusa klikove i drzi prozor otvoren
app.mainloop()



# while True:
#     # Izbornik
#     print("=== IZBORNIK ===")
#     print("Izaberite broj")
#     a = input("1. Dodaj knjigu\n"
#               "2. Dodaj člana\n"
#               "3. Posudi knjigu\n"
#               "4. Vrati knjigu\n")
#
#     #kreiranje knjige
#     if a == "1":
#         print("=== Unos nove knjige ===")
#         knjiga = Knjiga(input("Unesi naziv knjige: "),input("Unesi naziv autora: "))
#         knjiznica.dodaj_knjigu(knjiga)
#     #kreiraj clanovee
#     elif a == "2":
#         print("=== Unos novog člana ===")
#         clan = Clan(input("Ime: "), input("Godine: "), input("Email: "))
#         knjiznica.dodaj_clana(clan)
#     # posudi knjigu
#     elif a == "3":
#         print("=== Posuđivanje knjiga ===")
#         ime_clan= input("Ime člana: ")
#         naslov_knjiga = input("Unesite ime knjige: ")
#         knjiznica.posudi_knjigu(ime_clan, naslov_knjiga)
#     # vrati knjigu
#     elif a == "4":
#         print("=== Vrati knjigu ===")
#         ime_clan = input("Ime člana: ")
#         naslov_knjiga = input("Unesite ime knjige: ")
#         knjiznica.vrati_knjigu(ime_clan, naslov_knjiga)


