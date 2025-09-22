agenda={"Jherika": 999253614, "Joice": 99364791}
while True:
    print("-"*10)
    print("AGENDA")
    opcao=int(input("Digite a opção desejada \n1- ADICIONAR CONTATO \n2-BUSCAR CONTATO \n3-SAIR \n"))
    if opcao==1:
        contato=input("Qual nome do contato deseja adicionar? ").capitalize()
        telefone=input("Qual o seu número de telefone? ")
        agenda[contato]=[telefone]
        print(f"Sua nova lista de contatos é {agenda}")
    elif opcao==2:
        buscar=input("Qual contato deseja buscar? ").capitalize()
        if buscar in agenda:
            print(f"O número do contato é: {agenda[buscar]}")
        else:
            print("Contato não encontrado") 
    elif opcao==3:
        break
    else:
        print("Opção inválida")              
 
 
                        
        