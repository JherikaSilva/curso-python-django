""". Soma de Números Variáveis: Crie uma função que use *args para somar uma
quantidade qualquer de números."""

def soma_var(*numeros) ->int:
    """Soma de números variados"""
    total=0
    for numero in numeros:
        total+=numero
    return total

numeros=[]
while True:
    print("Para sair digite '0'")
    numero=int(input("Qual número deseja somar? "))
    if numero ==0:
        break
    else:
        numeros.append(numero)

resultado= soma_var(*numeros)      
print(f"O resultado da soma dos números da lista {numeros} é {resultado} ")  
    
        