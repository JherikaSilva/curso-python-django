"""Cálculo de Média: Crie uma função que receba três notas e retorne a média delas"""

def calcular_media(nota_1:float, nota_2:float,nota_3:float) -> float:
    """Calcular média de três notas"""
    return (nota_1+nota_2+nota_3)/3

nota_1=float(input("Digite a primeira nota: "))
nota_2=float(input("Digite a segunda nota: "))
nota_3=float(input("Digite a terceira nota: "))

resultado= calcular_media(nota_1, nota_2, nota_3)

print(f"O resultado médio das notas é {resultado:.2f} ")
    