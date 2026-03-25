def estadoNumero(linha):
  ponto = 0
  numero = []
  print(linha)
  for i in range(len(linha)):
    if linha[i] == '.':
      if ponto == 1:
        raise Exception("Número inválido")
      ponto += 1
    numero.append(linha[i])
  return "".join(numero)

def estadoOperador(linha):
  for i in range(len(linha)):
    if len(linha) > 1 and (linha[0] == "/") and (linha[1] == "/"):
       return "//"
    else:
      return linha[i]