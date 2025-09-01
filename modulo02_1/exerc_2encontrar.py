#Voce tem duas listas e precisa encontrar os elementos que aparecem em ambas. O programa deve gerar uma terceira lista contendo apenas os elementos em comum, sem repetiçoes
lista_1=["abacate", "melancia", "banana", "melao", "uva"]
lista_2=["melancia", "abobora", "uva", "morango","abacate"]
iguais=[]

for item in lista_1:
    if item in lista_2 and item not in iguais:
        iguais.append(item)
    
print(f"Os elementos em comum são {iguais}")
        