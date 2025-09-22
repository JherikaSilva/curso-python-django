#Limpeza de entrada, peça um texto com espaços no começo e no fim, use .strip para limpar e depois mostre o texto limpo

print("====== LIMPEZA DE ENTRADA ======")
texto= input("Digite um texto com espaços no começo e fim: ")
novo_texto= texto.strip()

print("O texto sem espaços é: ")
print(novo_texto)