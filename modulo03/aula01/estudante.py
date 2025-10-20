from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self._materias = {}

    def adicionar_nota(self, materia, nota):
        if materia in self._materias:
            self._materias[materia].append(nota)
        else:
            self._materias[materia] = [nota]

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nMatricula: {self.matricula}\nMaterias: {self._materias}"

    @property
    def materias(self):
        return self._materias

    @materias.setter
    def materias(self, valor):
        materia, indice, nova_nota = valor
        if materia in self._materias and 0 <= indice < len(self._materias[materia]):
            self._materias[materia][indice] = nova_nota
        
        
        
    
    