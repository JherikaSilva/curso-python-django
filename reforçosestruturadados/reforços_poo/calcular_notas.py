"""Cálculo de Média: Crie uma função que receba três notas e retorne a média delas"""

def calcular_media() -> float:
    """Calcular média de três notas"""
    
    nota_1=float(input("Digite a primeira nota: "))
    nota_2=float(input("Digite a segunda nota: "))
    nota_3=float(input("Digite a terceira nota: "))
    notas= nota_1+nota_2+nota_3
    
    return notas/3

resultado= calcular_media()
print(f"O resultado médio das notas é {resultado:.2f} ")
    