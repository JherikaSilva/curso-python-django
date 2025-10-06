

lista_numeros={10:"par", 15:"impar", 20:"par", 25:"impar"}

lista_par=[]
lista_impar=[]
for numero, valor in lista_numeros.items():
    if valor=="par":
        lista_par.append(numero)
    else:
        valor=="impar"
        lista_impar.append(numero) 
        
print(f"Os números da lista {lista_numeros} são pares {lista_par} e são ímpares {lista_impar}")        
       