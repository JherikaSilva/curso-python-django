import math


class Circulo:
    def __init__(self, raio):
        if raio > 0:
            self._raio= raio
        else:
            print("O raio não pode ser negativo")    
        
        
    @property
    def raio(self):
        return self._raio    
    
    @raio.setter
    def raio(self,novo_raio):
        if novo_raio > 0:
            self._raio=novo_raio
        else:
            self._raio=0
            
    def calcular_area(self):
        return math.pi *(self._raio **2)
        
    
    
circulo_1=Circulo(5)
area=circulo_1.calcular_area()
print(f"A area do circulo é {area:.1f}")

