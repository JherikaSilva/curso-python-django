
class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo= titulo
        self.duracao_seg=duracao_seg
        
    def exibir(self):
        print(f"Titulo: {self.titulo} \nDuração: {self.duracao_seg}\n")
        

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)      
        self.artista=artista
        
    def exibir(self):
        print(f"Titulo: {self.titulo} \nDuração: {self.duracao_seg} \nArtista: {self.artista}\n")  
        

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)      
        self.resolucao=resolucao
        
    def exibir(self):
        print(f"Titulo: {self.titulo} \nDuração: {self.duracao_seg} \nResolução: {self.resolucao}\n")
        

musica_1=Musica("Oceano", 3.10, "Djavan")
musica_2=Musica("Monalisa", 3.50, "Jorge Vercilo")
video_1=Video("Flor de Lis", 3.25, "4K")

dicionario:dict[Midia]={musica_1, musica_2, video_1}

for mid in dicionario:
    mid.exibir()