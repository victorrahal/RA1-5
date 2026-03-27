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
    valores = []
    for tokens in todosTokens:
        for token in tokens:
            if ValidarNumero(token):
                val = float(token)
                existente = False
                for v in valores:
                    if v == val:
                        existente = True
                        break
                if not existente:
                    valores.append(val)

    # cabeçalho seção data para definição dos valores doubles
    assembly.append(".global _start")
    assembly.append(".data")
    assembly.append(".align 3")
    for val in valores:
        x = f"val_{str(val).replace(".", "_")}"
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
                assembly.append(f"LDR R0 , ={x}")
                assembly.append(f"VLDR.F64 {reg}, [R0]") # carrega o valor no registrador
                pilhaReg.append(reg)  # empilha o registrador para uso futuro

            elif token in ['+', '-', '*', '/']:
                # desempilha os dois últimos operandos
                r2 = pilhaReg.pop()  # segundo operando
                r1 = pilhaReg.pop()  # primeiro operando
                # realiza a operação usando r1 como registrador de resultado
                match token:
                    case '+':
                        assembly.append(f"VADD.F64 {r1}, {r1}, {r2}")
                    case '-':
                        assembly.append(f"VSUB.F64 {r1}, {r1}, {r2}")
                    case '*':
                        assembly.append(f"VMUL.F64 {r1}, {r1}, {r2}")
                    case '/':
                        assembly.append(f"VDIV.F64 {r1}, {r1}, {r2}")

                pilhaReg.append(r1) # resultado volta para a pilha
                regsLivres.append(r2) #libera o registrador

    # finaliza o programa para não ficar em loop
    assembly.append("MOV R7, #1")
    assembly.append("SWI 0")
                
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
]

resultado = gerarAssembly(todosTokens, 'out.s')