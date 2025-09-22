from carro import Carro


carro=Carro("Corola", 10)
print(f"O carro modelo {carro.modelo} está com o nível de combustivel {carro.nivel_combustivel}")

while True:
        print("MENU")
        opcao=input("Escolha uma opção\n1-ABASTECER \n2-DIRIGIR\n3-SAIR\n")

        if opcao== "1":
            litros=int(input("Quantos litros quer abastecer: "))
            carro.abastecer(litros)

        elif opcao=="2":
            distancia=int(input("Quantos km irá percorrer: "))
            carro.dirigir(distancia)

        elif opcao=="3":
            print("Encerrando")
            break

        else:
            print("Opção inválida")          