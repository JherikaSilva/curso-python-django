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
            print(f"Seu saldo atual é de {saldo_inicial} e o seu limite é {limite_saldo}")
        elif opcao=="2":
            valor_a_sacr=float(input("Entre com o valor a ser sacado: "))
            if valor_a_sacr<= (saldo_inicial+limite_saldo):
                print("Saldo liberado, retire seu valor!")
                novo_saldo= saldo_inicial+limite_saldo-valor_a_sacr
                print(f"Seu novo saldo é {novo_saldo} ")
                saldo_inicial=novo_saldo
            else:
                print("Saldo insuficiente!")
        elif opcao=="3":
            depositar=float(input("Insira o valor a ser depositado: "))
            if depositar>0:
                saldo_inicial+=depositar
            else:
                print("Valor inválido!")    
        elif opcao=="4":
            boleto= float(input("Digite o valor do boleto: "))
            if boleto <=(saldo_inicial + limite_saldo):
                saldo_inicial-=boleto
            else:
                print("Saldo insuficiente")
        elif opcao=="5":
            senha_antiga=input("Digite a senha antiga: ")
            senha_nova1= input("Digite a nova senha: ")
            senha_nova2=input("Repita a nova senha: ")
            if senha_usuario==senha_antiga and senha_nova1== senha_nova2:
                senha_nova1 == senha_usuario
                print("Senha atualizado com sucesso.")
            else:
                print("Senha inválida. ")    
        elif opcao=="6":
            print("Atendimento Finalizado!")
            break
        else:
            print("Opção Inválida!")
            