class Clan:

    def __init__(self,id, name, age, email, ):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
    def __str__(self):
        return f"{self.name},{self.age},{self.email}"