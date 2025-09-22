#Encontre o segundo maior número em uma lista de números. O programa não pode usar o
#método .sort() da lista.

print("-------SEGUNDO MAIOR---------")
numeros=[10,20,15,30,25,5,40]
maior=0
segundo_maior=0
for i in numeros:
    if i>maior:
        segundo_maior=maior
        maior=i
    elif i<maior and  i>segundo_maior:
            segundo_maior=i

print(f"O segundo maior número da lista é {segundo_maior}")        