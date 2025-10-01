from estudante import Estudante

class Escola:
    def __init__(self):
        self.estud=[]
        
    def adicionar_estudante(self,estudante):
        self.estud.append(estudante)
    
    
    def mostrar_relatorio(self):
        for est in self.estud:
            print(f"Estudante: \n{est}")
        
           
        


       