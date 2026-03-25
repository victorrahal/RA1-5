from src.executarExpressao import executarExpressao

def teste_soma():
    tokens = ["(", "3.14", "2.0", "+", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert resultado == 5.14

def teste_multiplica():
    tokens = ["(", "1.5", "2.0", "*", ")"]
    memorias = {}
    res_anteriores = []
    resultado, memorias = executarExpressao(tokens, memorias, res_anteriores)
    assert resultado == 3.0