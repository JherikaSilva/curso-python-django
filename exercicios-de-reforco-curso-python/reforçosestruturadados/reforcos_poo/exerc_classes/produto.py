
class Produto:
    def __init__(self, nome, preco):
        self.nome=nome
        self.preco=preco


produto_1=Produto("Caderno",15.50)
produto_2=Produto("Caneta", 3.00)

print(f"O produto {produto_1.nome} custa R${produto_1.preco}")
print(f"O produto {produto_2.nome} custa R${produto_2.preco}")