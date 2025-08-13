#Senha com validação de letras e/ou números, peça uma senha e verifique com .isalnum() se ela contém apenas letras e/ou números

print("----- VALIDAÇÃO DE SENHA ------")
senha= input("Digite sua senha: ")
if senha.isalnum():
    print("Senha válida!")
else:
    print("Senha inválida")    