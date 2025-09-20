"""Crie uma classe chamada Pessoa. No "registro de nascimento" (__init__), toda pessoa deve
ter um nome e uma idade
"""
class Pessoa:
    def __init__ (self, nome, idade):
        self.nome= nome
        self.idade= idade



p1=Pessoa("João" , 25)
p2=Pessoa("Maria", 30)

print(f"Seu nome é: {p1.nome} e sua idade é: {p1.idade}")
print(f"Seu nome é: {p2.nome} e sua idade é: {p2.idade}")