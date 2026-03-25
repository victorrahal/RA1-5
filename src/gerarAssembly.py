def ValidarNumero(token):
    try:
        float(token) # verifica se é numero
        return True # retorna verdadeiro se for
    except ValueError:
        return False # retorna falso se não for numero

def gerarAssembly(tokens, arquivoSaida = 'out.s'):
    assembly = []
    numeros = []
    contadorNum = [0]

    k = 0
    # percorrer lista de tokens
    while k < len(tokens):
        token = tokens[k]

    # verifica se for um numero
    if ValidarNumero(token):
        marca = f"n{contadorNum[0]}"
        contadorNum[0] += 1 # aumenta contador de numeros
        numeros.append((marca, token)) # salva os numeros na lista de numeros