#Você tem uma lista de listas. Calcule a média de cada sublista e armazene os resultados em uma nova lista.

lista=[[10, 20, 30], [5, 10, 15], [1, 2, 3]]
nota_1=lista[0]
nota_2=lista[1]
nota_3=lista[2]
media=[]
media_1=sum(nota_1)/3  
media_2=sum(nota_2)/3
media_3=sum(nota_3)/3
media.append(media_1) 
media.append(media_2)
media.append(media_3)

print("====== Encontrando média ======")
print(f"\nA média das sublistas da lista {lista} é {media}")