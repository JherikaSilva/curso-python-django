"""Verificador de Número Par: Crie uma função que receba um número e retorne True se
ele for par e False se for ímpar.
"""
def verificar_par() -> bool:
    """Verificando se o número é par"""
    numero=int(input("Digite um número: "))
    if numero %2 == 0:
        par=True
    else:
        par=False
    print(par)        

verificar_par()        