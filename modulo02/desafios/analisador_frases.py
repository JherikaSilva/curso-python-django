
def quantidade_palavras(frase:str)-> int:
    """Para contar a quantidade de palavras de uma frase"""
    nova_frase=frase.split()
    return len(nova_frase)

def contar_vogais(frase:str) ->int:
    """Para contar vogais em frase"""
    vogais="a,e,i,o,u"
    cont=0
    for letra in frase:
        if letra in vogais:
            cont+=1
    return cont        

def contar_consoantes(frase:str) ->int:
    """Para contar consoantes em frase"""
    vogais="a,e,i,o,u"
    cont=0
    nova_frase=frase.replace(" ","")
    for letra in nova_frase:
        if letra not in vogais:
            cont+=1
    return cont     

def palindromo(frase:str) ->str:
    """Para analisar se a frase é um palíndromo"""
    nova_frase=frase.replace(" ","")
    frase_2=nova_frase[::-1]
    if nova_frase==frase_2:
        return "Sim"
    else:
        return "Não"
    
    

print("-"*30)
print("     ANALISADOR DE FRASES     ")
frase=input("Digite sua frase \n").lower()

print(f"A frase {frase}\ntem {quantidade_palavras(frase)} palavras\ntem {contar_vogais(frase)} vogais\ntem {contar_consoantes(frase)} consoantes\nÉ um palíndromo ? {palindromo(frase)}")   
