print("CONTADOR DE VOGAIS")
palavra=input("Digite uma palavra:").lower()
vogais="aeiou"
contador=0


for letra in palavra:
    if letra in vogais:
        contador+=1
print("O número total de vogais é: ", contador)    
    