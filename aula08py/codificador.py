""" crie um programa que codifica e decodifica uma frase, seguindo as regras abaixo 
cada vogal deve ser substituida a=1, e=2, i=3, o=4, u=5, o programa deve ler uma frase digitada pelo usuario, exibir a frase codificada trocando as vogais pelo numero
exibir a frase decodificada, voltando os numeros e vogais originais"""

print("-----CODIFICADOR DE FRASES-----")
frase=input("Digite sua frase: ").lower()
frase_codificada=frase.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
print(f"A frase codificada é: {frase_codificada}")
frase_deco=frase_codificada.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u")
print(f"E a frase decodificada é: {frase_deco}")
