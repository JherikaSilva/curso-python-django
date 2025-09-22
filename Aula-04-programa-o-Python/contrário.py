# Peça ao usuário para digitar uma palavra. Usando len e um laço while, imprima a palavra de trás para frente.
print("PALAVRA AO CONTRÁRIO")
palavra= input("Digite uma palavra: ")
cont=0
while cont<len(palavra):
    nova_palavra=palavra[::-1]
    cont+=1
print(nova_palavra)    
