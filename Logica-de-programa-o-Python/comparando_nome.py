#Comparando nomes ignorando minúsculas, peça dois nomes e verifique se são iguais usando .lower se forem iguais, mostre Nomes iguais, senão Nomes diferentes

print("---- COMPARADOR DE NOMES ----")
primeiro_nome= input("Digite o primeiro nome: ").lower()
segundo_nome= input("Digite o segundo nome: ").lower()

if primeiro_nome == segundo_nome:
    print("Nomes iguais")
else:
    print("Nomes diferentes")    