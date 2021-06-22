#!python3

from Validacao import nomeEhValido
from Aluno import Aluno

# Lista para armazenar os objetos do tipo Aluno
alunos = []

# Abrindo o arquivo contendo as notas dos alunos
arquivoAlunosNotas = open("alunosnotas.txt", "r")

# Percorrendo todas as linhas do arquivo
for linha in arquivoAlunosNotas.readlines():
  dados = linha.split(",")
  if nomeEhValido(dados[1]):
    # Criando um objeto do tipo 'Aluno'   
    aluno = Aluno()
    aluno.codigo = dados[0]
    aluno.nome = dados[1]
    aluno.notas.append(float(dados[2]))
    aluno.notas.append(float(dados[3]))
    aluno.notas.append(float(dados[4]))
    aluno.notas.append(float(dados[5]))

    # Adicionando o aluno a lista de alunos
    alunos.append(aluno)

# Fechando o arquivo  
arquivoAlunosNotas.close()  

# Gerando o boletim
boletins = open("boletimescolares.txt", "w")
for aluno in alunos:
  media = aluno.calcularMedia()
  situacao = aluno.obterSituacao(media)
  boletins.write(f"{aluno.codigo}, {aluno.nome}, {media:.2f}, {situacao}\n") 

boletins.close()
