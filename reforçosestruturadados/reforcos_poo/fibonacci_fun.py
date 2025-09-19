"""4. Gerador de Fibonacci: Crie uma função que receba um número inteiro n e retorne uma
lista com a sequência de Fibonacci até o n-ésimo termo."""

def fibonacci(numero:int)->list:
    """Função para uma lista de fibonacci"""
    a=0
    b=1
    cont=0
    soma=1 
    lista=[]
    while cont <= numero :
        lista.append(a)
        soma = a + b
        a = b
        b = soma
        cont+= 1
    print(lista)        
        

numero=int(input("Digite o número: "))  
print(f"\nA sequência de fibonacci até o {numero} termo é:")
fibonacci(numero)      