#Exerc 1
class Inventario:
    def __init__(self):
        self.lista_estoque=[]

    def adicionar_produto(self, produto, quantidade):
        if produto not in self.lista_estoque:
            item={
                "produto":produto,
                "quantidade":quantidade
            }
            self.lista_estoque.append(item)
        
        if self.produto in self.lista_estoque:
            self.lista_estoque[self.produto]=self.quantidade
       

    def remover_produto(self, produto):
        try:
            if produto in self.lista_estoque:
                self.lista_estoque.remove(produto)

        except ValueError:
            return "Produto não encontrado"      

    def vender_item(self, nome_produto, quantidade_vendida):
        if nome_produto in self.lista_estoque:
            while self.quantidade >0:
                for quant in self.lista_estoque:
                    estoque= quant - quantidade_vendida
                    self.quantidade= estoque


        




