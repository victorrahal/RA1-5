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

def estadoOperador(linha, i):
    if linha[i] == '/' and i+1 < len(linha) and linha[i+1] == '/':
        return "//", i+2
    else:
        return linha[i], i+1
  
def estadoComando(token):
    if not token.isalpha() or not token.isupper():
        raise Exception(f"Comando inválido: {token}")
    return token

def estadoIdentificador(linha, i):
    identificador = []
    while i < len(linha):
        char = linha[i]
        if char.isalpha() and char.isupper():
            identificador.append(char)
            i += 1
        else:
            break
    token = "".join(identificador)
    return estadoComando(token), i

def estadoParenteses(linha, i):
    return linha[i], i+1

def estadoInicial(linha, i):
    char = linha[i]
    if char.isdigit():
        return estadoNumero(linha, i)
    if char.isupper():
        return estadoIdentificador(linha, i)
    if char in ["+", "-", "*", "/", "%", "^"]:
        return estadoOperador(linha, i)
    if char in ["(", ")"]:
        return estadoParenteses(linha, i)
    if char == " ":
        return None, i + 1
    raise Exception(f"Caractere inválido: '{char}'")

def parseExpressao(linha):
    tokens = []
    i = 0
    while i < len(linha):
        token, i = estadoInicial(linha, i)
        if token is not None:
            tokens.append(token)
    return tokens