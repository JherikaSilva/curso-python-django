"""10. Contador de Vogais: Crie uma função que receba uma string e retorne o número de
vogais (a, e, i, o, u) que ela contém."""

def contar_vogais(frase:str) ->int:
    """Para contar vogais em frase"""
    vogais="a,e,i,o,u"
    cont=0
    for letra in frase:
        if letra in vogais:
            cont+=1
    return cont        

frase=input("Digite sua frase: ").lower()
resultado= contar_vogais(frase)
print(f"O número de vogais é {resultado}")