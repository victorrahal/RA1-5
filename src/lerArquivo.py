# FUNÇÃO LEITURA DO ARQUIVO TXT

def lerArquivo(nomeArquivo):
    linhas = []

    try:
        with open(nomeArquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha != "":
                    linhas.append(linha)

    except FileNotFoundError:
        print(f"Erro: arquivo '{nomeArquivo}' não encontrado.")
        return []
    
    except Exception as erro:
        print(f"Erro ao ler o arquivo '{nomeArquivo}': {erro}")
        return[]

    return linhas