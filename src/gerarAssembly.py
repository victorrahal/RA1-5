# Aluno 3: Lucas Balint Vilar

def ValidarNumero(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def gerarAssembly(todosTokens, arquivoSaida='out.s'):
    assembly = []

    assembly.append(".global _start")
    assembly.append(".text")
    assembly.append("_start:")

    regResult = 2  # registrador de resposta

    for tokens in todosTokens:
        pilhaReg = []
        primeiraOp = True
        regOp = 0  # controla r0 e r1

        for token in tokens:
            if token in ['(', ')']:
                continue

            if ValidarNumero(token):
                if primeiraOp:
                    # primeira operação usa r0 e r1
                    assembly.append(f"LDR r{regOp}, ={token}")
                    pilhaReg.append(f"r{regOp}")
                    regOp += 1
                else:
                    # depois sempre usa r0
                    assembly.append(f"LDR r0, ={token}")
                    pilhaReg.append("r0")

            elif token in ['+', '-', '*', '/']:

                if primeiraOp:
                    # primeira operação → r0 op r1
                    r1 = pilhaReg.pop()
                    r0 = pilhaReg.pop()

                    match token:
                        case '+':
                            assembly.append(f"ADD r{regResult}, {r0}, {r1}")
                        case '-':
                            assembly.append(f"SUB r{regResult}, {r0}, {r1}")
                        case '*':
                            assembly.append(f"MUL r{regResult}, {r0}, {r1}")
                        case '/':
                            assembly.append(f"SDIV r{regResult}, {r0}, {r1}")

                    pilhaReg.append(f"r{regResult}")
                    primeiraOp = False

                else:
                    # próximas operações caso seja aninhada
                    r0 = pilhaReg.pop()

                    match token:
                        case '+':
                            assembly.append(f"ADD r{regResult}, r{regResult}, {r0}")
                        case '-':
                            assembly.append(f"SUB r{regResult}, r{regResult}, {r0}")
                        case '*':
                            assembly.append(f"MUL r{regResult}, r{regResult}, {r0}")
                        case '/':
                            assembly.append(f"SDIV r{regResult}, r{regResult}, {r0}")

                    pilhaReg.append(f"r{regResult}")

        regResult += 1  # próximo token

    with open(arquivoSaida, 'w') as f:
        for linha in assembly:
            f.write(linha + '\n')

    return assembly

# TESTE
todosTokens = [
    ['(', '3', '2', '*', '3', '+', '4', '-', ')'],['(', '3', '2', '+', '3', '-', '4', '*', ')'],
    ['3', '2', '/']
]

resultado = gerarAssembly(todosTokens, 'out.s')