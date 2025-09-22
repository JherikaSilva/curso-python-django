"""Crie uma classe chamada Pessoa. No "registro de nascimento" (__init__), toda pessoa deve
ter um nome e uma idade

Adicione um método (uma "ação") à sua classe Pessoa chamado apresentar. Esse método
deve imprimir uma frase como: "Olá, meu nome é [nome] e eu tenho [idade] anos." Chame
esse método para os objetos "João" e "Maria"."""

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
