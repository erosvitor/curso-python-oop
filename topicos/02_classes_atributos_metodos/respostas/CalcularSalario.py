#!python3

class Funcionario:

  def __init__(self):
    self.nome = ""
    self.cargo = ""
    self.valorHora = ""

  def calcularSalario(self, horasTrabalhadas):
    return self.valorHora * horasTrabalhadas

func = Funcionario()
func.nome = "Fulano"
func.cargo = "Vendedor"
func.valorHora = 14.50

horasTrabalhadas = 30
salario = func.calcularSalario(horasTrabalhadas)

print("O salário é: ", salario)
