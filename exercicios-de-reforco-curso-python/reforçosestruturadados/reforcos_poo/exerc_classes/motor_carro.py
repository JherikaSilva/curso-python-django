class Motor:
    def __init__(self,potencial):
        self.potencial=potencial


class Carro:
    def __init__(self,modelo):
        self.modelo=modelo
        self.motor=Motor(200)

    def exibir_potencia(self):
        return self.motor.potencial    


carro=Carro("corola") 
print(f"O carro modelo {carro.modelo} tem {carro.exibir_potencia()} de potência")
       