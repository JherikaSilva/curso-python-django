"""Soma de Dois Números: Crie uma função que receba dois números e retorne a soma"""
def somar() ->int:
    """Função para somar números"""
    primeiro_numero=int(input("Digite o primeiro numero: "))
    segundo_numero=int(input("Digite o segundo numero: "))
    return primeiro_numero + segundo_numero

resultado=somar()
print(f"A soma dos números é {resultado}")
    
    
    