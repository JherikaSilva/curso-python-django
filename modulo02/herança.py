class Animal:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade
        
    def fazer_som(self):
        print("Metodo da classe super")    
        
class Cachorro(Animal):
    def __init__(self, nome, idade,raca):
        super().__init__(nome, idade)   
        self.raca=raca
        
    def fazer_som(self):
        print("Au, au")    
        
class Gato(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)             
        self.especie=especie
    
    def fazer_som(self):
        print("Miau")    

cachorro=Cachorro("Rex", 2, "salsicha")
gato=Gato("Dengo", 1, "frajola")

print(cachorro.nome)
cachorro.fazer_som()
print(gato.nome)
gato.fazer_som()        