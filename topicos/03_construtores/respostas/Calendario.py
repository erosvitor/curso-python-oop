#!python3

from datetime import datetime

class Calendario:

  def __init__(self, dataStr):
    data = datetime.strptime(dataStr, "%d/%m/%Y")
    self.dia = data.day
    self.mes = data.month
    self.ano = data.year
    self.diaSemana = data.weekday()

  def mesPorExtenso(self):
    meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", 
             "setembro", "outubro", "novembro", "dezembro")
    return meses[self.mes-1]

  def diaSemanaPorExtenso(self):
    nomeDiaSemana = ""
    if self.diaSemana == 0:
      nomeDiaSemana = "Segunda-feira"
    elif self.diaSemana == 1:
      nomeDiaSemana = "Terça-feira"
    elif self.diaSemana == 2:
      nomeDiaSemana = "Quarta-feira"
    elif self.diaSemana == 3:
      nomeDiaSemana = "Quinta-feira"
    elif self.diaSemana == 4:
      nomeDiaSemana = "Sexta-feira"
    elif self.diaSemana == 5:
      nomeDiaSemana = "Sabado"
    elif self.diaSemana == 5:
      nomeDiaSemana = "Domingo"
    return nomeDiaSemana    

  def dataPorExtenso(self):
    nomeDiaSemana = self.diaSemanaPorExtenso()
    nomeMes = self.mesPorExtenso()
    return f"{nomeDiaSemana}, {self.dia} de {nomeMes} de {self.ano}"

cal = Calendario("10/06/2021")
print(cal.mesPorExtenso())
print(cal.dataPorExtenso())

