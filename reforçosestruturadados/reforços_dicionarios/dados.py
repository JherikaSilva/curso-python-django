"""Dada uma lista de dicionários de produtos (com nome e preço),
encontre e imprima o nome e o preço do produto mais caro"""

produtos=[{"nome":"arroz","preço": 12.90 }, {"nome": "feijao","preço" :5.9} ,{"nome":"acucar","preço":3.9}, {"nome":"cafe", "preço":40}]

maior=0
produto_maior=""
for produto in produtos:
    if produto["preço"] > maior:
        maior=produto["preço"]
        produto_maior=produto["nome"]
        
print(f"O produto {produto_maior} é o mais caro e custa R${maior}")        
        