
class Funcionario:
    def __init__(self, nome,salario,percertual_bonus=10):
        self.nome=nome
        self.salario=salario
        self.percentual_bonus=percertual_bonus

    def aplicar_bonus(self):
        novo_salario=self.salario + (self.salario *self.percentual_bonus/100)
        self.salario= novo_salario


    
func_1=Funcionario("Marta", 1.500)   
func_2=Funcionario("Gustavo", 1.700)
print(f"Funcionária {func_1.nome} salário R${func_1.salario:.3f}")
print(f"Funcionária {func_2.nome} salário R${func_2.salario:.3f}")

func_1.aplicar_bonus()
func_2.aplicar_bonus()

print(f"Funcionária {func_1.nome} salário com bônus  R${func_1.salario:.3f}")
print(f"Funcionária {func_2.nome} salário com bônus  R${func_2.salario:.3f}")

