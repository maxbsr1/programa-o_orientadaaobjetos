class ConversorSimples:
    taxa_dolar = 5.25
    def real_para_dolar(self, valor_real):
        return valor_real / self.taxa_dolar
    
    def dolar_para_real(self, valor_dolar):
        return valor_dolar * self.taxa_dolar

conv = ConversorSimples()

print(conv.real_para_dolar(10))
print(conv.dolar_para_real(10))