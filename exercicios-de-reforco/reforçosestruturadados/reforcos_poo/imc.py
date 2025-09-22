"""Crie uma função que receba o peso (em kg) e a altura (em metros)
e retorne o Índice de Massa Corporal (IMC). A fórmula é: IMC = peso / (altura ** 2).
"""

def imc(peso:float, altura: float) ->float:
    """Função para calcular IMC"""
    imc=peso/(altura*altura)
    if imc < 18.5:
        print(f"Seu imc é {imc:.2f} 'Baixo peso'")
    elif  imc < 24.99 :
        print(f"Seu imc é {imc:.2f} 'Peso normal'")
    elif imc < 29.99 :
        print(f"Seu imc é {imc:.2f} 'Sobrepeso'")
    else:
        imc > 30
        print(f"Seu imc é {imc:.2f} 'Obesidade'")        
        
        
print("_"*20)
print("CALCULADORA IMC")

peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
imc(peso,altura)                