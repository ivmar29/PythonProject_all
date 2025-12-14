class Knjiga:
    def __init__(self, name, author, dostupno = True):
        self.name = name
        self.author = author
        self.dostupno = dostupno

    def __str__(self):
        return f"{self.name} - {self.author}"