print("---- LOGIN SIMPES ----")

usuario= input("Digite o usuário: ")
senha= input("Digite sua senha: ")
login= "admin"

if login in usuario and len(senha) >=6:
    print("Login autorizado")
else:
    print("Usuario ou senha incorretos")    