def num(token):
    try:
        float(token)
        return True
    except ValueError:
        return False
        
def operador(token):
    return token in ["+", "-", "*", "/", "//", "%", "^"]

def exec_operacao(a, b, operador):
    if operador == "+":
        return a + b
    if operador == "-":
        return a - b
    if operador == "*":
        return a * b
    if operador == "/":
        return a / b
    if operador == "//":
        return a // b
    if operador == "%":
        return a % b
    if operador == "^":
        return a ** b
    raise ValueError (f"Operação inválida: {operador}")

def executarExpressao (tokens, memorias, res_anteriores):
    pilha = []
    for token in tokens:
        if token in ["(", ")"]:
            continue
        if num(token):
            pilha.append(float(token))
        elif operador(token):
            if len(pilha) < 2:
                raise ValueError("Expressão Inválida: está faltando operadores")
            b = pilha.pop()
            a = pilha.pop()
            resultado = exec_operacao(a, b, token)
            pilha.append(resultado)
        else:
            # rever sobre mem e res
            pass
    if len(pilha) != 1:
        raise ValueError("Expressão Inválida: pilha incosistente")
    return pilha [0], memorias