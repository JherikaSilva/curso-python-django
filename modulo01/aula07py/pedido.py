#Crie um programa que simule um pedido em lanchonete
hamburguer=20.00
cupom="10"
while True:
    produto=input("Digite o seu pedido: ")
    if produto=="hamburguer":
        print("Pedido confirmado")
        break
    else:
        print("Esse lanche não esta cadastrado, tente novamente. ")

desconto=input("Digite seu cupom de desconto: ")
if desconto==cupom:
    print(f"Seu lanche custou: {hamburguer - hamburguer*0.10}") 
else:
    print(f"Seu lanche custou {hamburguer}")          