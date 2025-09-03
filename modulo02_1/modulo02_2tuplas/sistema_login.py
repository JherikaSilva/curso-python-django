#Você tem uma lista de tuplas, onde cada tupla é um registro de acesso(usuario, status, login), o status pode ser sucesso ou falha
#identifique e imprima o nome de usuarios que tiveram pelo menos 1 login bem sucedido, o nome dos usuarios que tiveram somente login com falhas

print("======== LOGIN ========")
acessos=[("Pedro","sucesso"),("Ana","falha"),("Maria","sucesso"),("Pedro","falha"),("Ana","falha")]
sucesso=set()
falha=set()

for nome,status in acessos:
    if status=="sucesso":
        sucesso.add(nome)
    elif status=="falha":
        falha.add(nome)
        
    som_falha=falha.difference(sucesso)
         
 

print(f"\n Usuários com pelo menos um login bem sucedido: {sucesso}")   
print(f"\n Usuários com login com falha: {som_falha}")        
                 
            