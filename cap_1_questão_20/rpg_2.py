class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar_oponente(self, alvo):
        print(f"{self.nome} ataca {alvo.nome} causando {self.ataque} de dano")
        alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

class Arena:
    def iniciar_batalha(self, personagem1, personagem2):
        print(f"🏟️ A batalha começa entre {personagem1.nome} e {personagem2.nome}!\n")

        rodada = 1
        while personagem1.esta_vivo() and personagem2.esta_vivo():
            print(f"--- Rodada {rodada} ---")
            personagem1.atacar_oponente(personagem2)

            if not personagem2.esta_vivo():
                break

            personagem2.atacar_oponente(personagem1)
            rodada += 1
            print()

        if personagem1.esta_vivo():
            print(f"\n {personagem1.nome} venceu a batalha")
        else:
            print(f"\n {personagem2.nome} venceu a batalha")

heroi = Personagem("Cristiano Ronaldo", 100, 20)
vilao = Personagem("Messi", 120, 15)

arena = Arena()
arena.iniciar_batalha(heroi, vilao)