#Peça ao usuário para digitar uma frase. Conte quantas vezes a palavra "a" aparece na frase (ignorando maiúsculas e minúsculas).
print("------ CAÇADOR DE PALAVRAS -----")
print("Vamos contar quantas vezes a letra 'A' aparece na sua frase")
letra_a= input("Digite sua frase: ").lower()
if "a" in letra_a:
    print("A letra 'A' aparece: ", letra_a.count("a"), "vezes!")
else:
    print("A frase não contém letra 'A' !")    
