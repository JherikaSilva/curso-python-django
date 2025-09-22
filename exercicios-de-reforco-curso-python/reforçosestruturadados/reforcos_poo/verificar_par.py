"""Verificador de Número Par: Crie uma função que receba um número e retorne True se
ele for par e False se for ímpar.
"""
def verificar_par(numero:int) -> bool:
    """Verificando se o número é par"""
    if numero %2 == 0:
        return True
    else:
        return False  
    
       
numero=int(input("Digite um número: "))
resultado=verificar_par(numero)
print(f"O número é par? {resultado}")        