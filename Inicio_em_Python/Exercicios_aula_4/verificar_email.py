#Peça ao usuário para digitar um email. Verifique e imprima se o email contém o caractere '@'.

print("----- VERIFICADOR DE EMAIL -----")
email= input("Digite seu email: ")

if "@" in email:
    print("O seu email contém o caractere '@' !")
else:
    print("O seu email não contém o caractere '@' !")    