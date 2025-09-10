class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar_oponente(self, alvo):
        print(f"{self.nome} ataca {alvo.nome} causando {self.ataque} de dano!")
        alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

heroi = Personagem("Herói", 100, 20)
monstro = Personagem("Monstro", 80, 15)

heroi.atacar_oponente(monstro)
monstro.atacar_oponente(heroi)