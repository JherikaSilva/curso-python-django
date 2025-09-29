class GraoCafe:
    def __init__(self):
        pass
    
    def moer(self):
       print("Os graos de cafe foram moidos") 
       
class Agua:
    def __init__(self):
        pass       
    
    def aquecer(self):
        print("A agua esta aquecida")
        
class Cafeteria:
    def __init__(self):
        self.grao_cafe=GraoCafe()
        self.agua=Agua()
        
    def preparar_cafe(self):
        print("Preparando cafe\n")
        self.grao_cafe.moer()
        self.agua.aquecer()
        print("\nO cafe esta pronto!")
        

cafe=Cafeteria()

cafe.preparar_cafe()       
    
              