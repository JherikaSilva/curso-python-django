from produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, quantidade_estoque, tempo_garantia_meses):
        super().__init__(nome, preco, quantidade_estoque)
        self.tempo_garantia= tempo_garantia_meses