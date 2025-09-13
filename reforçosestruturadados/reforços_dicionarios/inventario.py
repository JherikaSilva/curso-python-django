"""Crie um dicionário de inventário de um jogo (ex: "espada":
{"dano": 50, "peso": 2.5}). Permita que o usuário insira um item no inventário com suas caracteristicas e liste todos os itens"""

inventario={"espada":
    {"dado": 50, "peso":2.5}, 
    "bola":
    {"circunferencia": 68, "peso": 410}
    }
print("-"*12)
print(" INVENTÁRIO ")
print(inventario)
adicionar=input("Que produto deseja adicionar? \n")

if adicionar not in inventario:
    
    primeira_dimensao=input("Qual a primeira dimensão? \n")
    valor_primeira=float(input("Qual valor dela? \n"))
    segunda_dimensao=input("Qual a segunda dimensão? \n")
    valor_segunda=float(input("Qual valor dela? \n"))
    
    inventario[adicionar]= {
        primeira_dimensao: valor_primeira,
        segunda_dimensao: valor_segunda
    }
else:
    print("Esse produto já contém no inventário")
    
print(f"Inventário atualizado com sucesso \n{inventario}")        

