import random

class RoloDeDados:
    def rolar_d6(self):
        return random.randint(1, 6)

    def rolar_d12(self):
        return random.randint(1, 12)

    def rolar_d20(self):
        return random.randint(1, 20)

rolo = RoloDeDados()

print("Rolando D6:", rolo.rolar_d6())
print("Rolando D12:", rolo.rolar_d12())
print("Rolando D20:", rolo.rolar_d20())