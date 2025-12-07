class Clan:

    def __init__(self, name, age, email, id = None ):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
    def __str__(self):
        return f"{self.name},{self.age},{self.email}"