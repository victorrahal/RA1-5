# Aluno 4 - Paulo Henrique Eidi Mino

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lerArquivo import lerArquivo

def teste_len_arquivo_valido():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'src', 'arquivo3.txt')
    linhas = lerArquivo(caminho)
    assert len(linhas) > 0

def teste_len_ignora_linhas_vazias():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'src', 'arquivo3.txt')
    linhas = lerArquivo(caminho)
    for linha in linhas:
        assert linha.strip() != ""

def teste_arquivo_inexistente():
    linhas = lerArquivo("arquivo_que_nao_existe.txt")
    assert linhas == []

def teste_retorno_lista():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'src', 'arquivo3.txt')
    linhas = lerArquivo(caminho)
    assert isinstance(linhas, list)

def rodar_testes():
    teste_len_arquivo_valido()
    teste_len_ignora_linhas_vazias()
    teste_arquivo_inexistente()
    teste_retorno_lista()
    print("Todos os testes de arquivo passaram")

if __name__ == "__main__":
    rodar_testes()

