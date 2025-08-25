#Crie um programa que simula controle de um robô simples com menu de comandos
posicao=0

while True:
    opcao=input("Digite uma opção:\n"
            "1-AVANÇAR\n" \
            "2-RECUAR\n" \
            "3-STATUS\n"\
            "4-DESLIGAR\n")
    if opcao=="1":
        posicao+=1
        print(f"A sua nova posição é: {posicao}")
    elif opcao=="2":
        posicao-=1
        print(f"Sua nova posição é: {posicao}")
    elif opcao=="3":
        print(f"A sua posição é: {posicao}")
    elif opcao=="4":
        print("Programa desligado")
        break
    else:
        print("Opção inválida!")
        
