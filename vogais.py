#Peça ao usuário para digitar uma palavra. Usando um laço while, conte e imprima o número total de vogais (a, e, i, o, u) na palavra.

print("------ CONTADOR DE VOGAIS ------")
palavra= input("Digite uma palavra: ")
cont=1
while cont <=5:
    vogal_a= palavra.count("a")
    vogal_e= palavra.count("e")
    vogal_i= palavra.count("i")
    vogal_o= palavra.count("o")
    vogal_u= palavra.count("u")
    cont+=1
total=vogal_a+vogal_e+vogal_i+vogal_o+vogal_u    
print("o total de vogais é: ", total )
print("Sendo elas:")
print("Vogal 'A': ",vogal_a) 
print("Vogal 'E': ",vogal_e) 
print("Vogal 'I': ",vogal_i) 
print("Vogal 'O': ",vogal_o) 
print("Vogal 'U': ",vogal_u) 
      