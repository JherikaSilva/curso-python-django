preco = input ("Qual o preço original do produto? $")
float = float(preco)
desconto=0
if float > 100:
    desconto=10/100*float
    float= float-desconto
    print("O novo valor é: $" , float)
