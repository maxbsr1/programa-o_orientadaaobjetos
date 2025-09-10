class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} (Estoque: {self.estoque})"

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_produto(self, produto, quantidade):
        if quantidade <= produto.estoque:
            produto.estoque -= quantidade
            if produto.nome in self.itens:
                self.itens[produto.nome]["quantidade"] += quantidade
            else:
                self.itens[produto.nome] = {"produto": produto, "quantidade": quantidade}
            print(f"{quantidade}x '{produto.nome}' adicionado(s) ao carrinho.")
        else:
            print(f"Erro: Estoque insuficiente de '{produto.nome}'. Disponível: {produto.estoque}")

    def finalizar_compra(self):
        total = 0
        print("\nResumo da Compra:")
        for item in self.itens.values():
            produto = item["produto"]
            qtd = item["quantidade"]
            subtotal = produto.preco * qtd
            print(f"- {qtd}x {produto.nome} → R${subtotal:.2f}")
            total += subtotal
        print(f"Total da compra: R${total:.2f}")
        return total

p1 = Produto("Camisa", 79.90, 10)
p2 = Produto("Tênis", 199.90, 5)
p3 = Produto("Boné", 49.90, 2)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(p1, 2)
carrinho.adicionar_produto(p2, 1)
carrinho.adicionar_produto(p3, 5)

carrinho.finalizar_compra()

print("\nEstoque atualizado:")
print(p1)
print(p2)
print(p3)