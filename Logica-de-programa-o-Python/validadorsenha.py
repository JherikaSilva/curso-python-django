
print("----------- VALIDADOR DE SENHA ----------")


while True:
    senha= input("Digite sua senha: ")
    if senha [:].isupper():
        print("A senha deve conter letras maiúsculas ")
    elif senha[:].islower():
        print("A senha deve conter letras minúsculas")
    elif senha[:].isdigit():
        print("A senha deve conter números")



       