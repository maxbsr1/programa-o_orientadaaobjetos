class ConfiguracaoJogo:
    def __init__(self, resolucao_tela, volume_audio, dificuldade):
        self.resolucao_tela = resolucao_tela
        self.volume_audio = volume_audio
        self.dificuldade = dificuldade

config = ConfiguracaoJogo("1920x1080", 80, "Fácil")

print("Resolução:", config.resolucao_tela)
print("Volume:", config.volume_audio)
print("Dificuldade:", config.dificuldade)
