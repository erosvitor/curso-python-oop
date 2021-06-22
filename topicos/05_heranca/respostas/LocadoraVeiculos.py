#!python3

class Pessoa:

  def __init__(self):
    self.nome = ""
    self.endereco = ""
    self.telefone = ""

class PessoaFisica(Pessoa):

  def __init__(self):
    self.cpf = ""
    self.dataNascimento = ""

class PessoaJuridica(Pessoa):

  def __init__(self):
    self.cnpj = ""

class Cliente(PessoaFisica):
  pass

class Funcionario(PessoaFisica):

  def __init__(self):
    self.cargo = ""

class Veiculo:

  def __init__(self):
    self.marca = ""
    self.modelo = ""
    self.ano = 0
    self.cor = ""
    self.placa = ""
    self.km = 0

class Automovel(Veiculo):

  def __init__(self):
    self.portas = 0

class Moto(Veiculo):

  def __init__(self):
    self.cilindradas = 0


cliente = Cliente()
cliente.nome = "Fulano da Silva"
cliente.endereco = "Rua Sem nome, 999"
cliente.telefone = "41-998890110"
cliente.cpf = "102.113.609-37"
cliente.dataNascimento = "10/02/1982"

funcionario = Funcionario()
funcionario.nome = "Beltrano Gomes"
funcionario.endereco = "Av das coisas, 1000"
funcionario.telefone = "41-32002030"
funcionario.cpf = "215.079.299-00"
funcionario.dataNascimento = "05/12/1985"
funcionario.cargo = "Vendedor"

