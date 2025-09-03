class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

livro1 = Livro("O milionário da Caverna", "Doug Batchelor e Marilyn Tooker", 1999)
livro2 = Livro("A chave da virada", "Marcello Niek e Bruno Raso", 2024)

print(f"Título: {livro1.titulo}")
print(f"Autor: {livro1.autor}")
print(f"Autor: {livro2.autor}")
print(f"Ano de Publicação: {livro1.ano_publicacao}")
