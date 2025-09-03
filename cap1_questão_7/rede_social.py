class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

usuario1 = Usuario("Maxsuel Vasconcelos", "maxsuelbsr@gmail.com")
usuario2 = Usuario("Ana Ligia SIlva", "analigiashow@gmail.com")

print(usuario1.email)
print(usuario2.nome)
