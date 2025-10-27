#Exerc 1
class Inventario:
    def __init__(self):
        self.lista_estoque=[]

    def adicionar_produto(self, produto, quantidade):
        for item in self.lista_estoque:
            if item["produto"] == produto:
                item["quantidade"]+= quantidade
                return self.lista_estoque
                
        item_novo={
                "produto":produto,
                "quantidade":quantidade
                }
        self.lista_estoque.append(item_novo)
        return self.lista_estoque

                

    def remover_produto(self, produto):
        try:
            for item in self.lista_estoque:
                if item["produto"] == produto:
                    item_remover=item
                    self.lista_estoque.remove(item_remover)
                    return self.lista_estoque

        except ValueError:
            return "Produto não encontrado"      

    def vender_item(self, nome_produto, quantidade_vendida):
        if nome_produto in self.lista_estoque:
            while self.quantidade >0:
                for quant in self.lista_estoque:
                    estoque= quant - quantidade_vendida
                    self.quantidade= estoque


        




