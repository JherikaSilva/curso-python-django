
print(" ROTACIONANDO POSIÇÕES")
print("Iremos rotacinar duas posições do final para o início da sua lista!")

lista=[1,2,3,4,5,6,7]
lista_1=lista[-2:]
lista_2=lista[:-2]
lista_rotacionada=lista_1+lista_2

print(f"A lista {lista} rotacionada fica {lista_rotacionada}")