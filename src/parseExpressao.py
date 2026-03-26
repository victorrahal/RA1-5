def estadoNumero(linha, i):
    numero = []
    ponto = 0

    while i < len(linha):
        num = linha[i]
        if num.isdigit():
            numero.append(num)
        elif num == ".":
            if ponto > 1:
                raise Exception("Número inválido, mais de um ponto")
            ponto = 1
            numero += num
        else:
            break
        i = i + 1
    numero = "".join(numero)
    return numero, i

def estadoOperador(linha):
  for i in range(len(linha)):
    if len(linha) > 1 and (linha[0] == "/") and (linha[1] == "/"):
       return "//"
    else:
      return linha[i]
  
def estadoComando(linha):
  comando = []
  for i in range(len(linha)):
    entrada = linha[i]
    comando.append(entrada)
  if linha not in ["MEM","RES"]:
    raise Exception(f"Comando inválido")
  return linha