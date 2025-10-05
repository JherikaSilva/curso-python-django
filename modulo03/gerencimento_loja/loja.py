from produto import Produto
from produto_eletronico import ProdutoEletronico

class Loja:
    def __init__(self, lista_produtos:list[Produto][ProdutoEletronico]):   
        self.lista= lista_produtos
        self.estoque={}

    def adicionar_produto_estoque(self, produto, quantidade):
        if produto in self.estoque:
            self.estoque[produto].append(quantidade)
        else:
            self.estoque[produto]= [quantidade]

    def verificar_estoque_individual(self, produto):
        if produto in self.estoque:
            for produto, quant in produto.items():
                print(f"Produto: {produto} quantidade em estoque: {quant}")
        else:
            print("Produto não encontrado")        




    