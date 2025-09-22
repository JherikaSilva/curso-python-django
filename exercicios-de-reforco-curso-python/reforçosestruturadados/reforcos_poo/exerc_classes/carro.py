
class Carro:
    def __init__(self, modelo, nivel_combustivel=0):
        self.modelo=modelo
        self.nivel_combustivel=nivel_combustivel

    def abastecer(self,litros:int)->int:
        if litros > 0:
            novo_nivel= self.nivel_combustivel +litros
            self.nivel_combustivel = novo_nivel
            print(f"Carro abastecido com sucesso seu novo nível de combustivel é {novo_nivel}")
        else:
            print("Não é possível abastecer com números negativos")

    def dirigir(self,distancia):
        consumo= 10
        litros_necessarios= distancia/consumo

        if litros_necessarios <= self.nivel_combustivel:
            novo_nivel=self.nivel_combustivel-litros_necessarios
            self.nivel_combustivel=novo_nivel 
            print(f"Viagem realizada seu novo nivel de combustivel é :{novo_nivel}")

        else:
            print("Combustível insuficiente")



