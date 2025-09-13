"""Área de um Retângulo: Crie uma função que receba a base e a altura de um retângulo e
retorne sua área.
"""
def area_retangulo() ->float:
    """Retorna área de uma retângulo"""
    base=float(input("Digite a base do retângulo: "))
    altura=float(input("Digite a altura do retângulo: "))
    return base* altura

resultado = area_retangulo()
print(f"A área do retângulo é {resultado}")
