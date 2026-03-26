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

def estadoOperador(linha, i):
    if linha[i] == '/' and i+1 < len(linha) and linha[i+1] == '/':
        return "//", i+2
    else:
        return linha[i], i+1
  
def estadoComando(linha):
  comando = []
  for i in range(len(linha)):
    entrada = linha[i]
    comando.append(entrada)
  if linha not in ["MEM","RES"]:
    raise Exception(f"Comando inválido")
  return linha