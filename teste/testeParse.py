def estadoOperador(entrada, prox):
  for i in range(len(entrada)):
    if len(entrada) > 1 and (entrada[i] == '/') and (prox == '/'):
       return "//"
    else:
      return entrada[i]