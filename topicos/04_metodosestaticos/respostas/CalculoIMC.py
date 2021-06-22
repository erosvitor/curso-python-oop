class CalculoIMC:

  @staticmethod
  def calcularIndice(peso, altura):
    return peso / (altura * altura)

  @staticmethod
  def retornarClassificacao(imc):
    classificacao = ""
    if imc <= 18.5:
      classificacao = "Magro"
    elif imc <= 24.0:
      classificacao = "Normal"
    elif imc <= 29.9:
      classificacao = "Pré-obeso"
    else:
      classificacao = "Obeso"
    return classificacao

peso = 78
altura = 1.67

imc = CalculoIMC.calcularIndice(peso, altura)
classificacao = CalculoIMC.retornarClassificacao(imc)

print("IMC: {:.2f}".format(imc))
print("Classificacao: ", classificacao)
