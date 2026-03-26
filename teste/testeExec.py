from src.executarExpressao import executarExpressao

def teste_soma():
    tokens = ["(", "3.14", "2.0", "+", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 5.14) < 1e-9

def teste_subtracao():
    tokens = ["(", "3.14", "2.0", "-", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 1.14) < 1e-9

def teste_multiplica():
    tokens = ["(", "1.5", "2.0", "*", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 3.0) < 1e-9

def teste_divisao():
    tokens = ["(", "3.0", "4.0", "/", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 0.75) < 1e-9

def teste_resto():
    tokens = ["(", "5.0", "2.0", "%", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 1.0) < 1e-9

def teste_divisao_inteira():
    tokens = ["(", "5.0", "2.0", "//", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 1.0) < 1e-9

def teste_potencia():
    tokens = ["(", "3.0", "2.0", "^", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 9.0) < 1e-9

def teste_aninhado():
    tokens = ["(", "(", "3.0", "2.0", "*", ")", "(", "4.0", "2.0", "+", ")", "/", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 1.0) < 1e-9

def teste_mem():
    tokens = ["(", "5.0", "MEM", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 5.0) < 1e-9
    assert abs(memorias["MEM"] - 5.0) < 1e-9

def teste_len_mem():
    tokens = ["(", "MEM", "2.0", "+", ")"]
    memorias = {"MEM": 5.0}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 7.0) < 1e-9

def teste_mem_nao_inicializada():
    tokens = ["(", "VALOR", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 0.0) < 1e-9

def teste_res():
    tokens = ["(", "2", "RES", ")"]
    memorias = {}
    res_anteriores = [1.0, 2.0, 3.0]
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert abs(resultado - 3.0) < 1e-9

def teste_res_inexistente():
    tokens = ["(", "2", "RES", ")"]
    memorias = {}
    res_anteriores = [1.0, 2.0]
    try: 
        executarExpressao(tokens, memorias, res_anteriores)
        assert False
    except ValueError:
        assert True

def teste_token_invalido():
    tokens = ["(", "3.0", "2.0", "&", ")"]
    memorias = {}
    res_anteriores = []
    try:
        executarExpressao(tokens, memorias, res_anteriores)
        assert False
    except ValueError:
        assert True

def rodar_teste():
    teste_soma()
    teste_subtracao()
    teste_multiplica()
    teste_divisao()
    teste_resto()
    teste_divisao_inteira()
    teste_potencia()
    teste_aninhado()
    teste_mem()
    teste_len_mem()
    teste_mem_nao_inicializada()
    teste_res()
    teste_res_inexistente()
    teste_token_invalido()
    print("Todos os testes foram executados com sucesso")

if __name__ == "__main__":
    rodar_teste()