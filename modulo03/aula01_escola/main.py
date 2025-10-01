from estudante import Estudante
from escola import Escola


escola=Escola()
est_1=Estudante("Jherika", 27, 125545)
est_1.adicionar_nota("Matematica", 10)
est_1.adicionar_nota("Portugues", 8)
est_1.adicionar_nota("Matematica", 5)
escola.adicionar_estudante(est_1)
escola.mostrar_relatorio()