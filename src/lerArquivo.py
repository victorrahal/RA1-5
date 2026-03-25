# FUNÇÃO LEITURA DO ARQUIVO TXT

def lerArquivo(nomeArquivo):
    linhas = []

    try:
        with open(nomeArquivo, 'r') as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    linhas.append(linha)

    except FileNotFoundError:
        print(f"Erro: arquivo '{nomeArquivo}' não encontrado.")
        return []

    return linhas