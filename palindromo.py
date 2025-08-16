#Peça ao usuário para digitar uma palavra. Verifique se a palavra é um palíndromo (lida da mesma forma de trás para frente). Imprima "É um palíndromo" ou "Não é um palíndromo"
print("_________ PALÍNDROMO ________")
palavra= input("Digite sua palavra: ")
nova_palavra= palavra[::-1]
if nova_palavra==palavra:
    print("É um palíndromo! ")
else: 
    print("Não é um palíndromo")    