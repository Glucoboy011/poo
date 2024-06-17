from musico import Musico
from album import Album
class Banda:
    def __init__(self, nome):
        self.nome = nome
        self.musicos = []
        self.albuns = []
    def adicionar_musico(self, musico):
        self.musicos.append(musico)

    def remover_musico(self, musico_nome):
         self.musicos = [musico for musico in self.musicos if musico.nome != musico_nome]

    def mostrar_musicos(self):
        print(f'Banda: {self.nome}') 
        for musico in self.musicos: musico.mostrar_info() 
    
    def adicionar_album(self, album):
        self.albuns.append(album)

    def remover_album(self, album_titulo):
        self.albuns = [album for album in self.albuns if album.titulo != album_titulo]
    
    def mostrar_albuns(self):
        print(f"Álbuns da banda {self.nome}:")
        for album in self.albuns:
            print(album)