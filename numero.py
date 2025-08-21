#Crie um programa que solicita ao usuário um número e, em seguida imprima todos os números pares de 2 até o número digitado

print("---- NÚMEROS PARES ----")
numero=int(input("Digite um número: "))
for i in range(2,(numero+1),2):
    print(i)