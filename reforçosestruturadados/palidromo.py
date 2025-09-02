#Um palíndromo é uma sequência que lê o mesmo de trás para frente. Crie um programa que verifique se uma lista é um palíndromo.
print("-------PALÍNDROMO------")
lista=["a","b","c","b","a"]
nova_lista=lista[::-1]
if lista==nova_lista:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")    