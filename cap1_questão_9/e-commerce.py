class Produto:
    def __init__(self, nome, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = int(estoque)

p1 = Produto("Monitor", 300.00, 15)
p2 = Produto("Mouse", 50.00, 20)

print(p1.nome)
print(p2.estoque)
print(p1.preco)
