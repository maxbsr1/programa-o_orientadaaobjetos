class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao pedido de {self.cliente}.")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.itens)
        return total

p1 = Produto("Camisa", 79.90)
p2 = Produto("Tênis", 199.90)
p3 = Produto("Boné", 49.90)

pedido = Pedido("João")
pedido.adicionar_item(p1)
pedido.adicionar_item(p2)
pedido.adicionar_item(p3)

print(f"\nTotal do pedido de {pedido.cliente}: R${pedido.calcular_total():.2f}")