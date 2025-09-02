lista_1=[1,6,8,4,6,6,1]
nova_lista=[]
remover=6

for numero in lista_1:  
    nova=True
    if numero == remover:
        nova=False
    if nova:
        nova_lista.append(numero)

    
      
print(f"Essa é sua lista {lista_1} e essa é a lista com itens removidos {nova_lista}!")      