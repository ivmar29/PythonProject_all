import math

class Krug:
    def __init__(self, radius):
        self.radius = radius

    def povrsina(self):
        return math.pi * (self.radius ** 2)

    def opseg(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Krug s radijusom {self.radius}"

krug1 = Krug(5)
krug2 = Krug(3)

print(krug1)  # Ispis: Krug s radijusom 5
print(f"Površina: {krug1.povrsina():.2f}")
print(f"Opseg: {krug1.opseg():.2f}")