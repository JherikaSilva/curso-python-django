#Peça ao usuário para digitar uma frase e uma palavra. Verifique e imprima se a palavra está presente na frase

print("===== FRASE E PALAVRA =====")
frase= input("Digite sua frase: ")
palavra= input("Digite sua palavra: ") 

if palavra in frase:
    print("A sua palavra contém na frase!")
else:
    print("A sua palavra não contém na frase!")    
