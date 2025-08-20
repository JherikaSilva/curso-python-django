"""
programa de banco 
1-rodar em loop infinito
2-ter conta e senha(validar)
3-encerrar sessao
4-cheque especial(limite de saldo negativo)
5-tentar 3 vezes a senha
6-opçoes(saque, deposito, saldo)
7-mostrar saldo apos o saque
8-alterar senha
9-dizer o nome do usuario
10-pagar boleto

"""
#declaração
conta_corrente="123456-7"
senha_usuario="9999"
saldo_inicial=0
limite_saldo=500
nome_usuario="Jose"

while True:
    for i in range(3):
        conta=input("Entre com a sua conta corrente: ")
        senha=input("Entre com sua senha: ")
        if conta==conta_corrente and senha==senha_usuario:
            print(f"Bem vindo {nome_usuario}!")
            acesso_permitido=True
            break
        else: 
            print("Conta ou senha inválida")
            acesso_permitido=False
    if not acesso_permitido:
        break        
    while True:
        opcao=input("Escolha uma opção:\n" \
            "1-Ver saldo.\n" \
            "2-Sacar valor.\n" \
            "3-Depositar.\n"\
            "4-Pagar Boleto.\n" \
            "5-Alterar senha.\n" \
            "6-Sair. \n")
        if opcao=="1":
            pass
        elif opcao=="2":
            pass
        elif opcao=="3":
            pass
        elif opcao=="4":
            pass
        elif opcao=="5":
            pass
        elif opcao=="6":
            print("Atendimento Finalizado!")
            break
        else:
            print("Opção Inválida!")