#!python3

class Produto:

  def __init__(self):
    self.descricao = ""
    self.preco = 0

  def precoDistribuidor(self):
    return self.preco + (self.preco * (3/100))

  def precoRepresentante(self):
    return self.preco + (self.preco * (4.5/100))

  def precoConsumitor(self):
    return self.preco + (self.preco * (5.5/100))

prod = Produto()
prod.descricao = "Caneta"
prod.preco = 1.50

print("Preço distribuidor:", prod.precoDistribuidor())
print("Preço representante:", prod.precoRepresentante())
print("Preço consumidor:", prod.precoConsumitor())
