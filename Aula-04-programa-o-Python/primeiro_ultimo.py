# Peça ao usuário para digitar uma palavra. Se a palavra tiver mais de 5 caracteres, imprima o primeiro e o último caractere. Caso contrário, imprima a palavra inteira.
print("******* PRIMEIRO E ÚLTIMO *******")
palavra=input("Digite sua palavra: ")
if len(palavra) <=5:
    print("O primeiro caractere é: ",palavra[0]," e o último caractere é: ", palavra[-1])
else:
    print(palavra)
    print("A palavra tem mais que 5 caracteres!")    