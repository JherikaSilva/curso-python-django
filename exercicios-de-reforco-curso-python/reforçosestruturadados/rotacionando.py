#Crie um programa que rotacione uma lista para a direita por um determinado número de posições. Os elementos que saem do final da lista devem ir para o início.

#O número de posiçoes que ira rotacionar serão duas 
print(" ROTACIONANDO POSIÇÕES")
print("Iremos rotacinar duas posições do final para o início da sua lista!")

lista=[1,2,3,4,5,6,7]
lista_1=lista[-2:]
lista_2=lista[:-2]
lista_rotacionada=lista_1+lista_2

print(f"A lista {lista} rotacionada fica {lista_rotacionada}")