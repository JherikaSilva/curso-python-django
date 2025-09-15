"""Exercício 1: Analisador de Frases
Crie um programa que recebe uma frase do usuário e faz uma análise completa sobre ela,
mostrando:
● A quantidade de palavras na frase.
● A quantidade de vogais (a, e, i, o, u).
● A quantidade de consoantes.
● Se a frase é um palíndromo (ou seja, se ela pode ser lida da mesma forma de trás para
frente, ignorando espaços e letras maiúsculas).
"""

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

qnt_pal=quantidade_palavras(frase)
qnt_vog=contar_vogais(frase)
qnt_cons=contar_consoantes(frase)
palidr=palindromo(frase)     

print(f"A frase {frase}\ntem {qnt_pal} palavras\ntem {qnt_vog} vogais\ntem {qnt_cons} consoantes\nÉ um palíndromo ? { palidr}")   
