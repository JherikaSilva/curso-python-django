"""Área de um Retângulo: Crie uma função que receba a base e a altura de um retângulo e
retorne sua área.
"""
def area_retangulo(base:float, altura:float) ->float:
    """Retorna área de umaetângulo"""
    return base* altura


base=float(input("Digite a base do retângulo: "))
altura=float(input("Digite a altura do retângulo: "))

resultado = area_retangulo(base,altura)
print(f"A área do retângulo é {resultado}")
