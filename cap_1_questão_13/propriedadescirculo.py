import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio

circulo_magico = Circulo(5)
print(f"Área do círculo: {circulo_magico.calcular_area():.2f}")
print(f"Circunferência do círculo: {circulo_magico.calcular_circunferencia():.2f}")