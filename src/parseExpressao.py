import lerArquivo

def parseExpressao(linha):
    tokens = []
    i = 0
    pilha_parenteses = []
    while i < len(linha):
        entrada = linha[i]

        if entrada == ' ':
            i = i + 1
            continue

        elif entrada.isdigit():
            token, i = estadoNumero(linha, i)
            tokens.append(token)

        elif entrada in ['+','-','*','/','%','^']:
            token, i = estadoOperador(linha, i)
            tokens.append(token)

        elif entrada in "()":
            token, i = estadoParenteses(linha, i, pilha_parenteses)
            tokens.append(token)

        elif entrada.isalpha():
            token, i = estadoComando(linha, i)
            tokens.append(token)

        else:
            raise Exception(f"Entrada inválida")

    return tokens

def estadoNumero(linha, i):
    numero = []
    ponto = 0

    while i < len(linha):
        num = linha[i]
        if num.isdigit():
            numero.append(num)
        elif num == ".":
            if ponto >= 1:
                raise Exception("Número inválido, mais de um ponto")
            ponto = 1
            numero += num
        else:
            break
        i = i + 1
    numero = "".join(numero)
    return numero, i
  
def estadoComando(linha, i):
    letras = []

    while i < len(linha) and linha[i].isalpha():
        letras.append(linha[i])
        i = i + 1
    comando = "".join(letras)
    if comando not in ["MEM", "RES"]:
        raise Exception(f"Comando inválido não bate com a máquina de estados")

    return comando, i

def estadoOperador(linha, i):
    if linha[i] == '/' and i+1 < len(linha) and linha[i+1] == '/':
        return "//", i+2
    else:
        return linha[i], i+1

def estadoParenteses(linha, i):
    return linha[i], i+1

def estadoParenteses(linha, i, pilha):
  if linha[i] == "(":
    pilha.append("(")
  elif linha[i] == ")":
    if not pilha:
      raise Exception("Parenteses não batem")
    pilha.pop()
  return linha[i], i+1

def parseMultiplas(expressoes):
    resultado = []

    for expr in expressoes:
        tokens = parseExpressao(expr)
        resultado.append(tokens)

    return resultado

lista = lerArquivo.lerArquivo("src/arquivo1.txt")
resultado = parseMultiplas(lista)
print(resultado)