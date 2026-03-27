# Arquivo de funções de utilidade para deixar o arquivo main() mais enxuto

import sys
import os
import json

# Função responsável por validar as linhas de comando informadas, onde o programa
# recebe exclusivamente UM argumento, sendo ele o arquivo de teste
def validarArgumentos() -> str:
    if len(sys.argv) != 2:
        print("Erro, o programa aceita exclusivamente um arquivo\nExemplo: python3 main.py <teste1.txt>")
        sys.exit(1)

    nomeArquivo = sys.argv[1]

    if not os.path.isfile(nomeArquivo):
        print(f"Erro, {nomeArquivo} não foi encontrado")
        sys.exit(1)

    if os.path.getsize(nomeArquivo) == 0:
        print(f"Erro, {nomeArquivo} está vazio")
        sys.exit(1)

    return nomeArquivo

# Função responsável por salvar os tokens gerados em um arquivo .json
def salvarTokens(tokens_todas_linhas: list[list[str]], nomeArquivoSaida: str) -> None:
    dados = {
        "total_linhas": len(tokens_todas_linhas),
        "tokens_por_linha": []
    }
    for i, tokens in enumerate(tokens_todas_linhas):
        dados["tokens_por_linha"].append({
            "linha": i + 1,
            "tokens": tokens
        })
 
    with open(nomeArquivoSaida, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
 
    print(f"Tokens salvos em: {nomeArquivoSaida}")

# Função responsável por salvar o código Assembly gerado em um arquivo .s (utilizado no CPULATOR)
def salvarAssembly(codigoAssembly: str, nomeArquivoSaida: str) -> None:
    with open(nomeArquivoSaida, 'w', encoding='utf-8') as f:
        f.write(codigoAssembly)

    print(f"Código Assembly salvo em: {nomeArquivoSaida }")