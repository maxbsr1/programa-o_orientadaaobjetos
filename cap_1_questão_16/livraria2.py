class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

class Livraria:
    def __init__(self):
        self.catalogo = {}

    def adicionar_livro(self, livro):
        if livro.titulo not in self.catalogo:
            self.catalogo[livro.titulo] = livro
            print(f"Livro {livro} adicionado ao catálogo.")
        else:
            print(f"O livro '{livro.titulo}' já está no catálogo.")

    def buscar_livro(self, titulo):
        if titulo in self.catalogo:
            return self.catalogo[titulo]
        else:
            print(f"O livro '{titulo}' não foi encontrado no catálogo.")
            return None

livro1 = Livro("O Ceticismo da Fé", "Rodrigo SIlva")
livro2 = Livro("Deus e o vazio humano", "Rodrigo SIlva")

livraria = Livraria()
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

resultado = livraria.buscar_livro("O Ceticismo da fé")
if resultado:
    print("Livro encontrado:", resultado)

livraria.buscar_livro("Escavando a verdade")