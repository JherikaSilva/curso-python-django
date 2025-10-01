

class Retangulo:
    def __init__(self, base,altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
       """Para calcular area de um retangulo"""
       return self.base*self.altura   

    def calcular_perimetro(self):
        """Para calcular perimetro de um retangulo"""
        return 2 *(self.base+self.altura)


Ret=Retangulo(25, 30)
area=Ret.calcular_area()
perimetro=Ret.calcular_perimetro()

print(f"A area do retangulo e {area} e o perimetro e {perimetro}")