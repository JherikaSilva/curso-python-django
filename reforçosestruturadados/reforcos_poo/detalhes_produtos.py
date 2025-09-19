"""16. Detalhes do Produto: Crie uma função que receba o nome de um produto e use
**kwargs para exibir detalhes adicionais como preço, marca e estoque.
"""

def produtos(**detalhes):
    for chave,valor in detalhes.items():
        print(f"{chave}:{valor}")
        

nome=input("Digite o nome do produto: ")
marca=input("Digite a marca do produto: ")
estoque=input("Digite quanto tem de estoque: ")
produtos(nome=nome, marca=marca,estoque=estoque)        