class Musica:
    def __init__(self, titulo, artista):
        self.titulo= titulo
        self.artista= artista


class Playlist:
    def __init__(self, list_music:list[Musica]):
        self.musicas=list_music
    
    def adicionar_musica(self, nome_music:Musica):
        self.musicas.append(nome_music)    
        
    def remover_musica(self, nome_music:Musica):
        self.musicas.remove(nome_music) 
    
    def tocar_playlist(self):
        pass       
        