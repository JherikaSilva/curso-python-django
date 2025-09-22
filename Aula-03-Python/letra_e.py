# Peça ao usuário para digitar uma palavra e imprima a posição (índice) da primeira letra 'e' que ele encontrar.

print("==== LETRA 'E' ====")
palavra= input("Digite sua palavra: " )

if "e" in palavra:
    print("A primeira letra 'e' está na posiçao", palavra.find("e")+1,"!")