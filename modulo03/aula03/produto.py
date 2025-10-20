class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome= nome
        self._preco= preco
        self._quantidade= quantidade_estoque

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        """Setter para atualizar o preço do produto."""
        self._preco = novo_preco

    @property
    def quantidade(self):
        return self._quantidade   
    @preco.setter
    def quantidade(self, nova_quantidade):
        """Setter para atualizar o quantidade em estoque do produto."""
        self._quantidade = nova_quantidade