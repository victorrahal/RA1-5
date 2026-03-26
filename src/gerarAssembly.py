#Aluno 3: Lucas Balint Vilar

def ValidarNumero(token):
    try:
        float(token) # verifica se é numero
        return True # retorna verdadeiro se for
    except ValueError:
        return False # retorna falso se não for numero

def gerarAssembly(todosTokens, arquivoSaida = 'out.s'):
    assembly = [] # lista instruções assemblu
    

    assembly.append(".global _start")
    assembly.append(".text")
    assembly.append("_start:")

    # percorrer lista de tokens
    for tokens in todosTokens:
        pilha = [] # pilha para rastreas os registradores
        ContRegs = 0 # contador para nomear os regs
        for token in tokens:
            if token in ['(', ')']: # ignora parenteses
                continue

            # verifica se for um numero
            if ValidarNumero(token):
                reg = f"R{ContRegs}" # cria o registrador R0, R1, etc
                assembly.append(f'LDR {reg}, ={token}') # gera a instrução para carregar o numero no registrador
                pilha.append((reg)) # empilha registrador
                ContRegs += 1 # aumenta contador dos ContRegses

            elif token in ['+', '-', '*', '/']:
                r2 = pilha.pop() #pega o ultimo registrador
                r1 = pilha.pop() #pega o penultimo registrador

                match token:
                    case '+':
                        assembly.append(f'ADD {r1}, {r1}, {r2}') # r1 = r1 + r2
                    case '-':
                        assembly.append(f'SUB {r1}, {r1}, {r2}') # r1 = r1 + r2
                    case '*':
                        assembly.append(f'MUL {r1}, {r1}, {r2}') # r1 = r1 * r2
                    case '/':
                        assembly.append(f'SDIV {r1}, {r1}, {r2}') # r1 = r1 / r2 )


    with open(arquivoSaida, 'w') as f:
        for linha in assembly:
            f.write(linha + '\n')

    return assembly

todosTokens = [['(', '3', '2', '+', ')'], ['(', '3', '2', '-',')'],
               ['(', '3', '2', '*', ')'], ['(', '3', '2', '/',')']]
resultado = gerarAssembly(todosTokens)
print(resultado)