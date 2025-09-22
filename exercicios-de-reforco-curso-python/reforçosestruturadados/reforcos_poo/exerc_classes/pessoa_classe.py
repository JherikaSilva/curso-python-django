
class Pessoa:
    def __init__ (self, nome, idade):
        self.nome= nome
        self.idade= idade

    def apresentar(self):
        "Um print com nome e idade"
        print(f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos")    




p1=Pessoa("João" , 25)
p2=Pessoa("Maria", 30)

p1.apresentar()
p2.apresentar()
