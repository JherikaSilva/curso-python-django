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
        for item in self.lista_estoque:
            if item["produto"] == produto:
                self.lista_estoque.remove(item)
                return self.lista_estoque

    
        raise ValueError("Produto não encontrado")

    def vender_item(self, nome_produto, quantidade_vendida):
        for produtos in self.lista_estoque:
            if produtos["produto"] == nome_produto:
                quant_estoque = produtos.get("quantidade", 0)
                # Verifica se há estoque suficiente antes de realizar a venda
                if quantidade_vendida > quant_estoque:
                    raise ValueError("Quantidade indisponível")
                quant_estoque -= quantidade_vendida
                produtos["quantidade"] = quant_estoque
                return self.lista_estoque

        raise ValueError("Produto não encontrado")
            




        




