#Peça ao usuário para digitar uma senha. Verifique se a senha, tem pelo menos 8 caracteres. Imprima "Senha válida" ou "Senha inválida"

print("======= VALIDADOR DE SENHA =======")
senha= input("Digite uma senha: ")
if len(senha) >=8:
    print("Senha válida! ")
else:
    print("Senha inválida, deve conter pelo menos 8 caracteres! ")    