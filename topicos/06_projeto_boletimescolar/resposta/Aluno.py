
class Aluno:
  
  # Atributos
  def __init__(self):
    self.codigo = ""
    self.nome = ""
    self.notas = []

  # Métodos
  def calcularMedia(self):
    totalNotas = 0
    for nota in self.notas:
      totalNotas += nota
    media = totalNotas / 4
    return media

  def obterSituacao(self, media):
    situacao = ""
    if media >= 70.0:
      situacao = "Aprovado"
    elif media >= 40:
      situacao = "Recuperação"
    else:
      situacao = "Reprovado"
    return situacao
