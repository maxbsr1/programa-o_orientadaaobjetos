class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        print(f"Música '{musica}' adicionada à playlist '{self.nome}'.")

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print(f"Música '{musica}' removida da playlist '{self.nome}'.")
        else:
            print(f"A música '{musica}' não está na playlist.")

    def listar_musicas(self):
        print(f"\nPlaylist: {self.nome}")
        if not self.musicas:
            print("Nenhuma música na playlist.")
        else:
            for i, musica in enumerate(self.musicas, start=1):
                print(f"{i}. {musica}")

minha_playlist = Playlist("Favoritas")
minha_playlist.adicionar_musica("Digno - Adoradores 5")
minha_playlist.adicionar_musica("Intensamente - Adoradores 5")
minha_playlist.listar_musicas()
minha_playlist.remover_musica("Digno - Adoradores 5")
minha_playlist.listar_musicas()