"""Desafio de Programação: Validação de Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo."""

print("------TRIÂNGULO------")
lado_1a=input("Digite o primeiro valor: ")
lado_1b=input("Digite o segundo valor: ")
lado_1c=input("Digite o terceiro valor: ")
if lado_1a.isdigit() and lado_1b.isdigit() and lado_1c.isdigit():
    lado_1a=int(lado_1a) 
    lado_1b=int(lado_1b) 
    lado_1c=int(lado_1c)
    if lado_1a<= 0 and lado_1b<=0 and lado_1c<=0:
        print("Os valores tem que ser positivos")
else:
    print("Os valores tem que ser somente números")  

valores_somados=True
if lado_1a> lado_1b+lado_1c or lado_1b> lado_1a+lado_1c or lado_1c> lado_1a+ lado_1b:
    valores_somados=False

abs_dife=True
if abs(lado_1b-lado_1c)>lado_1a or abs(lado_1a-lado_1c)>lado_1b or abs(lado_1a-lado_1b)>lado_1c:
    abs_dife=False
           

if valores_somados==True and abs_dife== True:
    print("Os valores podem formar um triangulo")
else:
    print("Os valores não podem formar um triangulo")    

