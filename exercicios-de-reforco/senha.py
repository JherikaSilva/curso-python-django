senha="python123"
while True:
    senha_usuario=input("Digite sua senha: ")
    if senha_usuario==senha:
        print("Senha correta, acesso autorizado.")
        break
    else:
        print("Senha incorreta, tente novamente.")