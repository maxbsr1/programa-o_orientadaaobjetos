class GeradorDeLog:
    def info(self, mensagem):
        return f"[INFO] - {mensagem}"

    def alerta(self, mensagem):
        return f"[ALERTA] - {mensagem}"

    def erro(self, mensagem):
        return f"[ERRO] - {mensagem}"

log = GeradorDeLog()

print(log.info("Sistema iniciado."))
print(log.alerta("Uso de memória acima do esperado."))
print(log.erro("Falha ao conectar ao banco de dados."))