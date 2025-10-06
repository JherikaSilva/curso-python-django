

tarefas={"dicionarios": ["pendente","em andamento","concluido"], "funcoes": ["pendente","em andamento","concluido"]}

print("-"*30)
print("    ADICIONANDO TAREFAS    ")
print(f"\n{tarefas} \n")

adicionar=input("Que tarefa deseja adicionar? \n")

if adicionar not in tarefas:
    
    primeiro_status=input("Qual primeiro status da tarefa? \n")
    segundo_status=input("Qual segundo status da tarefa? \n")
    terceiro_status=input("Qual terceiro status da tarefa? \n")
    
    tarefas[adicionar]= [primeiro_status, segundo_status, terceiro_status]
else:
    print("Esse tarefa já contém na lista")

print(f"Tarefa adicionada com sucesso a lista \n{tarefas}")    