"""Crie uma classe Retangulo que é inicializada com base e altura. Crie dois métodos:
1. calcular_area(): deve retornar o cálculo base * altura.
2. calcular_perimetro(): deve retornar o cálculo 2 * (base + altura).
Crie um retângulo, chame os dois métodos e imprima os resultados que eles retornam."""

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