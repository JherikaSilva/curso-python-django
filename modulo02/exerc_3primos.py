#Sua tarefa é criar um programa que percorra uma lista de numeros e crie uma nova lista contendo apenas os numeros que forem primos
numeros=[1,2,3,4,5,6,7,8,9,10]
primo=[]

for numero in numeros:
    primo_verd=True
    if numero<2:
        primo_verd=False    
    else:
        for i in range(2,numero):
            if numero % i ==0:
                primo_verd=False
                break
    if primo_verd:
        primo.append(numero)
                
print(f" A lista{numeros} tem esses numeros primos {primo}")        
    