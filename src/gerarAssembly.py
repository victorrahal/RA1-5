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


    ContRegs_Result = 2 # contatodor dos registradores de resultados inicia em 2 (R2)
    # percorrer lista de tokens
    for tokens in todosTokens:
        valores = [] # cria lista que vai salvar os numeros
        for token in tokens:
            if token in ['(', ')']: # ignora parenteses
                continue

            # verifica se for um numero
            if ValidarNumero(token):
                valores.append(token) # coloca o numero na lista

            elif token in ['+', '-', '*', '/']:
                assembly.append(f'LDR R0, ={valores[0]}')
                assembly.append(f'LDR R1, ={valores[1]}')
                regResult = f'R{ContRegs_Result}'

                match token:
                    case '+':
                        assembly.append(f'ADD {regResult}, R0, R1') # Rx = R0 + R1
                    case '-':
                        assembly.append(f'SUB {regResult}, R0, R1') # Rx = R0 - R1
                    case '*':
                        assembly.append(f'MUL {regResult}, R0, R1') # Rx = R0 * R1
                    case '/':
                        assembly.append(f'SDIV {regResult}, R0, R1') # Rx = R0 / R1

                ContRegs_Result += 1 # aumenta contador do registrador de resultado
                valores = [] # zera lista de numeros para seguir para os próximos tokens    


    with open(arquivoSaida, 'w') as f:
        for linha in assembly:
            f.write(linha + '\n')

    return assembly

todosTokens = [['(', '3', '2', '+', ')'], ['(', '3', '2', '-',')'],
               ['(', '3', '2', '*', ')'], ['(', '3', '2', '/',')']]
resultado = gerarAssembly(todosTokens)
print(resultado)