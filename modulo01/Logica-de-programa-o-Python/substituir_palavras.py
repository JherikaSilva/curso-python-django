#Sibstituindo palavras, peça uma frase e uma palavra a substituir, depois peça a nova palavra e use replace para fazer a troca

("------- SUBSTITUINDO PALAVRAS -------")

frase= input("Digite sua frase: ")
palavra= input("Digite a palavra que quer substituir: ")
nova_palavra= input("Por qual palavra? ")
print("A frase substituída é: ")
print ((frase).replace(palavra , nova_palavra))