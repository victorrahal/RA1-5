# Aluno 3: Lucas Balint Vilar

def ValidarNumero(token):
    try:
        float(token)  
        return True   # se True é numero
    except ValueError:
        return False  # se der erro, não é número


def gerarAssembly(todosTokens, arquivoSaida='out.s'):
    assembly = []  # lista que armazena as instruções assembly

    # cabeçalho padrão
    assembly.append(".global _start")
    assembly.append(".text")
    assembly.append("_start:")

    for tokens in todosTokens:# percorre cada expressão
        pilhaReg = []  # pilha que armazena registradores em uso
        regsLivres = []
        for k in range(12):
            regsLivres.append(f"r{k}")   
                 
        for token in tokens: # percorre cada token da expressão
            if token in ['(', ')']:
                continue  # ignora parênteses

            if ValidarNumero(token):
                reg = regsLivres.pop(0) # pega o primeiro registrador livre
                assembly.append(f"LDR {reg}, ={token}")  # carrega o valor no registrador
                pilhaReg.append(reg)  # empilha o registrador para uso futuro

            elif token in ['+', '-', '*', '/']:
                # desempilha os dois últimos operandos
                r2 = pilhaReg.pop()  # segundo operando
                r1 = pilhaReg.pop()  # primeiro operando
                # realiza a operação usando r1 como registrador de resultado
                match token:
                    case '+':
                        assembly.append(f"ADD {r1}, {r1}, {r2}")
                    case '-':
                        assembly.append(f"SUB {r1}, {r1}, {r2}")
                    case '*':
                        assembly.append(f"MUL {r1}, {r1}, {r2}")
                    case '/':
                        assembly.append(f"SDIV {r1}, {r1}, {r2}")

                pilhaReg.append(r1) # resultado volta para a pilha
                assembly.append(f'LDR {r2}, = 0') #libera o registrador
                
    # escreve o código assembly no arquivo de saída
    with open(arquivoSaida, 'w') as f:
        for linha in assembly:
            f.write(linha + '\n')

    return assembly  # retorna a lista

todosTokens = [
    ['3', '2', '5', '*', '+'],                  # (3 + (2*5))
    ['4', '2', '*', '6', '5', '*', '-'],        # (4*2) - (6*5)
    ['10', '5', '+', '1', '3', '*', '-']        # (10+5) - (1*3)
]

resultado = gerarAssembly(todosTokens, 'out.s')