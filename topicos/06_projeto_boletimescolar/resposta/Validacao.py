
# Função para verificar se um nome é válido ou não
def nomeEhValido(nome):
  nomeValido = True  
  for i in range(0, len(nome)):
    caractere = nome[i]
    if not caractere.isalpha() and not caractere.isspace():
      nomeValido = False
      break;
  return nomeValido
  