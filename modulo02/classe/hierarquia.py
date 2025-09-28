
class FormaGeometrica:
    def __init__(self, cor):
        self.cor=cor

    def calcular_area(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, cor, __largura, __altura):
        super().__init__(cor)
        self.__largura=__largura
        self.__altura=__altura

    def get_largura(self):
        return self.__largura 

    def get_altura(self):
        return self.__altura

    def set_largura(self, nova_largura):
        self.__largura=nova_largura

    def set_altura(self, nova_altura):
        self.__altura=nova_altura       

    def calcular_area(self):
        return self.__largura*self.__altura


class Quadrado(Retangulo):
    def __init__(self, cor, lado):
        super().__init__(cor,lado,lado)        
        self.lado=lado


        



retangulo=Retangulo("laranja", 20, 10)
quadrado=Quadrado("azul",10)

formas=(retangulo, quadrado)

def calcular_soma_area(formas):
    soma=0
    for item in formas:
        soma+=item.calcular_area()
        print(f"O objeto {item.cor} tem a área {soma}")

calcular_soma_area(formas)