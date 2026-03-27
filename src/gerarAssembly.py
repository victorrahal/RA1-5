# Aluno 3: Lucas Balint Vilar

def ValidarNumero(token):
    try:
        float(token)  
        return True   # se True é numero
    except ValueError:
        return False  # se der erro, não é número


def gerarAssembly(todosTokens, arquivoSaida='out.s'):
    assembly = []  # lista que armazena as instruções assembly

    # validar valores únicos para não dar conflito na compilação do assembly
    valores = [] # lista que armazena valores únicos
    for tokens in todosTokens:
        for token in tokens:
            if ValidarNumero(token):
                val = float(token)
                existente = False # variavel para verificar se o valor ja existe
                for v in valores:
                    if v == val: # faz a verificação
                        existente = True
                        break # se existir sai do loop
                if not existente:
                    valores.append(val) # se nao existe adiciona na lista de valores unicos

    # cabeçalho seção data para definição dos valores doubles
    assembly.append(".global _start")
    assembly.append(".data")
    assembly.append(".align 3")
    for val in valores:
        x = f"val_{str(val).replace(".", "_")}" # cria a label do valor
        assembly.append(f"{x}: .double {val}")

    # cabeçalho padrão
    assembly.append(".text")
    assembly.append(".arm")
    assembly.append(".fpu vfpv3")
    assembly.append(".align 2")        
    assembly.append("_start:")

    for tokens in todosTokens:# percorre cada expressão
        pilhaReg = []  # pilha que armazena registradores em uso
        regsLivres = []
        for k in range(8):
            regsLivres.append(f"D{k}")   
                 
        for token in tokens: # percorre cada token da expressão
            if token in ['(', ')']:
                continue  # ignora parênteses

            if ValidarNumero(token):
                reg = regsLivres.pop(0) # pega o primeiro registrador livre
                val = float(token)
                x = f"val_{str(val).replace(".", "_")}"
                assembly.append(f"LDR R0, ={x}") # carrega o endereço de x em R0
                assembly.append(f"VLDR.F64 {reg}, [R0]") # carrega o valor no registrador
                pilhaReg.append(reg)  # empilha o registrador para uso futuro

            elif token in ['+', '-', '*', '/', '//', '%']:
                # desempilha os dois últimos operandos
                r2 = pilhaReg.pop()  # segundo operando
                r1 = pilhaReg.pop()  # primeiro operando
                # realiza a operação usando r1 como registrador de resultado
                match token:
                    case '+':
                        assembly.append(f"VADD.F64 {r1}, {r1}, {r2}") # operacao de soma
                    case '-':
                        assembly.append(f"VSUB.F64 {r1}, {r1}, {r2}") # oepracao de subtração
                    case '*':
                        assembly.append(f"VMUL.F64 {r1}, {r1}, {r2}") # operacao de multiplicação
                    case '/':
                        assembly.append(f"VDIV.F64 {r1}, {r1}, {r2}") # operação de divisão não inteira
                    case '//':
                        assembly.append(f"VDIV.F64 {r1}, {r1}, {r2}") # divisão não inteira
                        assembly.append(f"VCVT.S32.F64 S0, {r1}") # converte para inteiro, truncando o float
                        assembly.append(f"VCVT.F64.S32 {r1}, S0") # volta o resultado para double
                    case '%': # resto: A - (A/B) * B
                        assembly.append(f"VDIV.F64 D6, {r1}, {r2}") # divisão não inteira
                        assembly.append(f"VCVT.S32.F64 S0, D6") # converte para inteiro, truncando o float
                        assembly.append(f"VCVT.F64.S32 D6, S0") # volta o resultado para double
                        assembly.append(f"VMUL.F64 D6, D6, {r2}") # (A/B) * B
                        assembly.append(f"VSUB.F64 {r1}, {r1}, D6") # A - (A/B) * B

                pilhaReg.append(r1) # resultado volta para a pilha
                regsLivres.append(r2) #libera o registrador

    # finaliza o programa para não ficar em loop
    assembly.append("    MOV R7, #1")
    assembly.append("    SWI #0")
                
    # escreve o código assembly no arquivo de saída
    with open(arquivoSaida, 'w') as f:
        for linha in assembly:
            f.write(linha + '\n')

    return assembly  # retorna a lista

todosTokens = [
    ['3.14', '2', '5', '*', '+'],                 
    ['4', '2.5', '*', '6', '5', '*', '-'],        
    ['10', '5.0', '+', '1', '3.57', '*', '-'],        
    ['10', '5', '/'],
    ['10', '3', '//'],
    ['10', '3', '%']
]

resultado = gerarAssembly(todosTokens, 'out.s')