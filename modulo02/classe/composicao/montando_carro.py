class Motor:
    def ligar(self):
        print("O motor ligou")
        
class Carro:
    def __init__(self):
        self.motor=Motor()
    
    def ligar_carro(self):
        self.motor.ligar()
                    
                    
corola=Carro()

corola.ligar_carro()                    