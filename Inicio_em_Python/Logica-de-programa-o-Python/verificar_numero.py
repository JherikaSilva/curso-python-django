#Verificaçao de número, peça algo ao usuário e use .isdigit() para verificar se ele apenas digitou números

print("------- VERIFICADOR DE NÚMERO -------")
texto=input("Digite algo: ")
if texto.isdigit():
    print("O texto só contém números")
else:
    print("O texto não contém só números ")    