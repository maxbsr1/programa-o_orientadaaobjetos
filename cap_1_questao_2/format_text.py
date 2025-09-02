class FormatadorDeTexto:
    def para_caixa_alta(self, texto):
        return texto.upper()

    def para_caixa_baixa(self, texto):  
        return texto.lower()

fmt = FormatadorDeTexto()

print(fmt.para_caixa_alta("Bem-vindo a minha página!"))
print(fmt.para_caixa_baixa("Bem-vindo a minha página!"))