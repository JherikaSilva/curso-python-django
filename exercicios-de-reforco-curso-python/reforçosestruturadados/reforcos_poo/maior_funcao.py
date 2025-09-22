""" Encontrar o Maior Número: Crie uma função que receba uma lista de números e
retorne o maior número da lista. Use um loop. Se a lista estiver vazia, retorne None.
"""
from typing import Optional
def maior_num(numeros:list[int]) -> Optional[int]:
    """Para ver qual o maior número de uma lista"""
    if not numeros:
        return None
    maior=numeros[0]
    for num in numeros:
        if num>maior:
            maior=num
    return maior


numeros=[]
while True:
    print("Para sair digite '0' ")
    numero=int(input("Digite o número: "))
    if numero == 0:
        break
    else:
        numeros.append(numero)

resultado= maior_num(numeros)
print(f"O maior número digitado da lista {numeros} é {resultado}")        
        
