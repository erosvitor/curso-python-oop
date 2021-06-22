#!python3

class ContaCorrente:

  def __init__(self, numero = None, saldo = None, limite = None):
    self.numero = numero
    self.saldo = 0 if saldo == None else saldo
    self.limite = 500 if limite == None else limite

  def depositar(self, valor):
    self.saldo += valor

  def sacar(self, valor):
    if self.saldo >= valor:
      self.saldo -= valor
      return True
    else:
      return False

  def consultarSaldo(self):
    return self.saldo

conta1 = ContaCorrente("0101-02", 5000, 1000)
conta1.depositar(1000)
conta1.sacar(570)

print(conta1.consultarSaldo())
