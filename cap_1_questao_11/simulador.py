class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O carro freou. Velocidade atual: {self.velocidade} km/h")

meu_carro = Carro()
meu_carro.acelerar(50)
meu_carro.frear(20)
meu_carro.frear(40)