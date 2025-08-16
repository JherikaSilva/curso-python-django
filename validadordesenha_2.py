# Peça ao usuário para digitar uma senha. Verifique se a senha contém a palavra "senha". Se contiver, imprima "Senha fraca", caso contrário, imprima "Senha forte".

print("======= VALIDADOR DE SENHA =======")
senha= input("Digite uma senha: ")
palavra="senha"
if palavra in senha:
    print("Senha fraca!")
else:
    print("Senha forte")    