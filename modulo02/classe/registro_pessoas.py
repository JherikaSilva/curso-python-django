
class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
        
    def apresentar(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n")
        

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)            
        self.curso=curso
        
    def apresentar(self):
           print(f"Nome: {self.nome} \nIdade: {self.idade} \nCurso: {self.curso}\n")



p_1=Pessoa("Marta", 25)
est_1=Estudante("Jherika", 27, "Python")

lista:list[Pessoa]=[p_1, est_1]

for pess in lista:
    pess.apresentar()