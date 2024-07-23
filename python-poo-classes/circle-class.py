import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def circunferencia(self):
        return 2 * math.pi * self.raio


circulo = Circulo(7)
print("Área:", circulo.area())
print("Circunferência:", circulo.circunferencia())
