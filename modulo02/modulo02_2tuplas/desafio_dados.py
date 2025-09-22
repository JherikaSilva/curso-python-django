"""Desafio: Análise de Dados de Acessos
Sua tarefa é processar um fluxo de dados de acessos de usuários, identificando informações
importantes e tratando possíveis erros. O programa deve pedir ao usuário para inserir dados
de acesso, que consistem em um nome de usuário, um status de acesso e um número que
representa a duração da sessão em minutos.
O usuário pode inserir quantos acessos quiser. Para parar a inserção de dados, ele deve
digitar "parar".
1. Armazene cada acesso válido como uma tupla (usuário, status, duracao_minutos).
2. Adicione essas tuplas a uma lista chamada registros_acessos.
3. Use um conjunto para armazenar todos os usuários que tiveram pelo menos um
acesso bem-sucedido.
4. No final, calcule e imprima o tempo total de todas as sessões bem-sucedidas.
"""
print("------- ANALISES DE DADOS --------")

acessos_sucessos = []
soma = 0 
todos_acessos=[] 

while True : 
    acesso_valido = [] 
    usuario = input("Para sair digite PARAR \nDigite o nome do usuário:").lower() 
    if usuario == "parar": 
        break 
    usuario=usuario.capitalize()
    acesso_valido.append(usuario)
    
    while True: 
      status = input("Digite o status do usúario: \n 1-SUCESSO ou 2-FALHA \n") 

      if  status != "1" and status != "2": 
        print("Status inválido. Tente novamente.") 
         
      if status == "1": 
        status = "Sucesso" 
        acesso_valido.append(status) 
        acessos_sucessos.append(usuario) 
        break 
      if status == "2": 
        status = "Falha" 
        acesso_valido.append(status)  
        break 
    while True: 
     try: 
      duracao_minutos = int(input("Digite o tempo de sessão em minutos: ")) 
      if duracao_minutos >= 0: 
         acesso_valido.append(duracao_minutos) 
         break 
     except ValueError: 
      print("Comando inválido, digite apenas números") 

    if status == "Sucesso" or status== "1": 
         soma+=duracao_minutos  
       
    acesso_valido=tuple(acesso_valido)   
    todos_acessos.append(acesso_valido) 
 
        

print(f"Os acessos digitados foram: \n{todos_acessos}") 
print(f"Os usuários com sucesso foram: \n{acessos_sucessos}") 
print(f"O tempo total de usuários com sucesso foi: \n{soma}") 

 