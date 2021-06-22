#!python3

class CalculoJuros:

  @staticmethod
  def jurosSimples(capital, taxa, periodo):
    return capital * (taxa/100) * periodo

  @staticmethod
  def jurosCompostos(capital, taxa, periodo):
    taxa /= 100
    return capital * (1 + taxa) ** periodo

jurosSimples = CalculoJuros.jurosSimples(1000, 10, 1)
print("Juros simples: ", jurosSimples)

jurosCompostos = CalculoJuros.jurosCompostos(1000, 10, 1)
print("Juros compostos: ", jurosCompostos)
