# Caça-Letras: Peça ao usuário para digitar uma frase e uma letra. Usando while, encontre todas as posições (índices) onde a letra aparece na frase e imprima-as.
print("________ CAÇA LETRAS ________")
frase=input("Digite uma frase: ")
letra=input("Digite uma letra: ")
i=0
caractere=0
while i<len(frase):
    if letra in frase[i]:
        caractere+=1
    else:
        caractere+=0
    i+=1
print("A letra aparece ", caractere, "vezes!")            
