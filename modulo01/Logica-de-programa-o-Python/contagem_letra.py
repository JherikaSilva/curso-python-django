#Contagem de letra específica, peça um texto e uma letra mostre quantas vezes a letra aparece usando .count

print("------- CONTADOR DE LETRAS ------")
texto= input("Digite uma texto: ")
letra= input("Digite qual letra quer contar? ")
contagem= texto.count(letra) 
print("A letra aparece", contagem, "vezes")