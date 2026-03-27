import os

from utils import validarArgumentos, salvarTokens, salvarAssembly, exibirResultados

# Criar e importar o módulo lerArquivo.py com a função lerArquivo(nomeArquivo),
# que recebe o caminho de um arquivo e retorna uma lista de strings (uma por linha).

# Criar e importar o módulo parseExpressao.py com a função parseExpressao(linha),
# que recebe uma linha de texto e retorna uma lista de tokens (análise léxica).

# Criar e importar o módulo executarExpressao.py com a função executarExpressao(tokens, memoria, historico),
# que recebe os tokens, um dicionário de memória e uma lista de histórico,
# avalia a expressão e retorna o resultado numérico.

# Criar e importar o módulo gerarAssembly.py com a função gerarAssembly(tokens_todas_linhas),
# que recebe a lista de tokens de todas as linhas e retorna uma string
# contendo o código Assembly correspondente.

from lerArquivo import lerArquivo

linhas = lerArquivo("arquivo1.txt")
print(linhas)

def main():
    # Valida os argumentos da linha de comando, garantindo que o usuário informou
    # um arquivo válido e existente. Retorna o nome do arquivo a ser processado.
    nomeArquivo = validarArgumentos()
    print(f"Processando o arquivo: {nomeArquivo}")

    # Lê o conteúdo do arquivo de entrada e separa em uma lista de linhas.
    # Se houver qualquer erro na leitura, exibe a mensagem e encerra a execução.
    try:
        linhas = lerArquivo(nomeArquivo)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    print(f"Linhas lidas: {len(linhas)}")

    # Percorre cada linha do arquivo e realiza a análise léxica (tokenização)
    # através do parseExpressao. Os tokens de cada linha são armazenados em uma
    # lista. Caso ocorra um erro léxico, a linha recebe uma lista vazia.
    tokens_todas_linhas = []
    for i, linha in enumerate(linhas):
        try:
            tokens = parseExpressao(linha)
            tokens_todas_linhas.append(tokens)
            print(f"Linha {i+1}: {tokens}")
        except Exception as e:
            print(f"Erro léxico na linha {i+1}: {e}")
            tokens_todas_linhas.append([])

    # Executa cada expressão tokenizada, mantendo um dicionário de memória para
    # variáveis e um histórico de resultados anteriores. Linhas vazias ou com erro
    # recebem o valor padrão 0.0.
    memoria = {}
    historico = []
    resultados = []

    for i, tokens in enumerate(tokens_todas_linhas):
        if not tokens:
            resultados.append(0.0)
            historico.append(0.0)
            continue
        try:
            resultado, memoria = executarExpressao(tokens, memoria, historico)
            resultados.append(resultado)
            historico.append(resultado)
        except Exception as e:
            print(f"Erro ao executar linha {i+1}: {e}")
            resultados.append(0.0)
            historico.append(0.0)

    # Exibe os resultados de todas as expressões processadas para o usuário.
    exibirResultados(resultados)

    # Gera o código Assembly a partir dos tokens e salva em um arquivo .s,
    # utilizando o mesmo nome base do arquivo de entrada.
    try:
        nomeBase = os.path.splitext(nomeArquivo)[0]
        codigoAssembly = gerarAssembly(tokens_todas_linhas)
        salvarAssembly(codigoAssembly, f"{nomeBase}.s")
    except Exception as e:
        print(f"Erro ao gerar Assembly: {e}")

    # Salva os tokens de todas as linhas em um arquivo JSON, permitindo
    # consulta posterior da análise léxica realizada.
    try:
        nomeBase = os.path.splitext(nomeArquivo)[0]
        salvarTokens(tokens_todas_linhas, f"{nomeBase}_tokens.json")
    except Exception as e:
        print(f"Erro ao salvar tokens: {e}")
 
 
if __name__ == "__main__":
    main()