
class Comodo:
    def __init__(self, nome):
        self.nome=nome
    
    
class Casa:
    def __init__(self,list_comodos:list[Comodo]):
        self.comodos=list_comodos
        
    def adicionar_comodo(self, nome_com:Comodo):
        self.comodos.append(nome_com)   
        
    def listar_comodos(self):
        for comodo in self.comodos:
            print(comodo.nome)


casa=Casa([])
casa.adicionar_comodo(Comodo("Sala"))
casa.adicionar_comodo(Comodo("Cozinha"))
casa.adicionar_comodo(Comodo("Quarto"))

casa.listar_comodos()

         