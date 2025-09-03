#Voce tem uma lista de vendas, onde cada venda é uma tupla, 
# crie uma nova lista chamada vendas contendo apenas as tuplas onde o valor total de venda é maior ou igual a 100
#crie um conjunto com todoos os nomes de produtos unicos da lista original

print("===== FILTRAGEM E ANÁLISE DE DADOS =====")
vendas=[("Teclado",50,2),("Mouse",25.50,4),("Monitor",300,1),("Fone",45,1),("Webcam",75.20,2)]
vendas_filtradas=[]
produtos_unicos=set()

for produto,valor,qnt in vendas:
    total=valor*qnt
    if total>=100:
        vendas_filtradas.append((produto,valor,qnt)) 
        
    produtos_unicos.add(produto) 
     
print(f"As vendas maiores que $100 foram {vendas_filtradas}")
print(f"E os produtos foram {produtos_unicos}")          
       