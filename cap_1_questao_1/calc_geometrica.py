class CalculadoraGeometrica:
    def calcular_area_quadrado(self, lado):
        return lado * lado

    def calcular_area_circulo(self, raio):
        pi= 3.1415
        return pi * (raio * raio)

calc = CalculadoraGeometrica()
        
print("area quadrado", calc.calcular_area_quadrado(5))
print("area circulo", calc.calcular_area_circulo(3))