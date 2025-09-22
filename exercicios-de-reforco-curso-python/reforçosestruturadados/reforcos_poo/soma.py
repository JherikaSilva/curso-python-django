"""Soma de Dois Números: Crie uma função que receba dois números e retorne a soma"""
def somar(primeiro_num:int, segundo_num:int) ->int:
    """Função para somar números"""
    return primeiro_num + segundo_num

primeiro_num=int(input("Digite o primeiro numero: "))
segundo_num=int(input("Digite o segundo numero: "))
resultado=somar(primeiro_num, segundo_num)
print(f"A soma dos números é {resultado}")
    
    
    