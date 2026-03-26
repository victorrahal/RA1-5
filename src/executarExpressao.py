def num(token):
    try:
        float(token)
        return True
    except (ValueError, TypeError):
        return False
        
def operador(token):
    return token in ["+", "-", "*", "/", "//", "%", "^"]

def identificar_mem(token);
    return token.isalpha() and token.isupper() and token != "RES"

def validar_int(token):
    if not num(token):
        raise ValueError(f"Valor inválido para RES: {token}")
    valor = float(token)
    if not valor.is_integer():
        raise ValueError(f"RES não pode ter índice negativo: {token}")
    return valor

def buscar_memoria(nome_mem, memorias):
    if nome_mem not in memorias:
        raise ValueError(f"Memória não iniciada: {nome_mem}")
    return memorias[nome_mem]

def buscar_res_anterior(indice, res_anteriores):
    if indice >= len(res_anteriores):
        raise ValueError("Não há resultados anteriores suficientes para RES")
    return res_anteriores[-(indice + 1)]

def validar_operadores_int(a, b, operador):
    if not float(a).is_integer() or not float(b).is_integer():
        raise ValueError(f"O operador '{operador}' é necessário valor inteiro")
    return int(a), int(b)

def exec_operacao(a, b, operador):
    if operador == "+":
        return a + b
    if operador == "-":
        return a - b
    if operador == "*":
        return a * b
    if operador == "/":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero")
        return a / b
    if operador == "//":
        a_int, b_int = validar_operadores_int(a, b, operador)
        if b_int == 0:
            raise ZeroDivisionError("Divisão por zero")
        return a_int // b_int
    if operador == "%":
        a_int, b_int = validar_operadores_int(a, b, operador)
        if b_int == 0:
            raise ZeroDivisionError("Resto por zero")
        return a_int % b_int
    if operador == "^":
        if not float(b).is_integer():
            raise ValueError("O expoente da potência necessita ser inteiro")
        expoente = int(b)
        if expoente < 0:
            raise ValueError("O expoente da potência não pode ser negativo")
        return a ** expoente
    raise ValueError (f"Operação inválida: {operador}")

def avaliar_tokens(tokens_limpos, memorias, res_anteriores):
    pilha = []
    i = 0
    while i < len(tokens_limpos):
        token = tokens_limpos[i]
        if num(token) and i + 1 < len(tokens_limpos) and tokens_limpos[i + 1] == "RES":
            indice = validar_int(token)
            valor = buscar_res_anterior(indice, res_anteriores)
            pilha.append(float(valor))
            i += 2
            continue
        if num(token):
            pilha.append(float(token))
            i += 1
            continue
        if identificar_mem(token):
            valor = buscar_memoria(token, memorias)
            pilha.append(float(valor))
            i += 1
            continue
        if operador(token):
            if len(pilha) < 2:
                raise ValueError("Expressão inválida: está faltando operadores")
            b = pilha.pop()
            a = pilha.pop()
            resultado = exec_operacao(a, b, token)
            pilha.append(float(resultado))
            i += 1
            continue
        if token == "RES":
            raise ValueError("Uso incorreto do RES")
        raise ValueError(f"Token inválido neste arquivo: {token}")
    if len(pilha) != 1:
        raise ValueError("Expressão inválida: pilha inconsistente")

    return pilha[0]

def executarExpressao (tokens, memorias, res_anteriores):
    pilha = []
    tokens_limpos = [token for token in tokens if token not in ["(", ")"]]
    if len(tokens_limpos) == 0:
        raise ValueError("Expressão vazia")
    if len(tokens_limpos) > 1 and identificar_mem(tokens_limpos[-1]):
        nome_mem = tokens_limpos[-1]
        exp_valor = tokens_limpos[:-1]
        valor = avaliar_tokens(exp_valor, memorias, res_anteriores)
        memorias[nome_mem] = float(valor)
        return float(valor), memorias
    
    resultado = avaliar_tokens(tokens_limpos, memorias, res_anteriores)
    return float(resultado), memorias