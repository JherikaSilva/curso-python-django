
class Pessoa:
    def __init__(self, nome, idade):
        self._nome=nome
        self._idade=idade
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
        if isinstance(novo_nome, str) and novo_nome:
             self._nome = novo_nome
        else:
            print("Nome inválido")
        

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,nova_idade):
        if isinstance(nova_idade, int) and nova_idade > 0: 
            self._idade=nova_idade
        else:
            print("Idade inválida")    
            
       
    

pessoa_1=Pessoa("Maria" , 10)
print(f"A pessoa {pessoa_1.nome} tem {pessoa_1.idade} anos")
pessoa_1.nome="João"
pessoa_1.idade=20
print(f"A pessoa {pessoa_1.nome} tem {pessoa_1.idade} anos")




