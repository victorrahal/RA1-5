# Aluno 2 - Victor Rahal Basseto

from src.parseExpressao import parseExpressao

def teste_exp_soma():
    tokens = parseExpressao("(3.14 2.0 +)")
    assert tokens == ["(", "3.14", "2.0", "+", ")"]

def teste_exp_aninhada():
    tokens = parseExpressao("((1.5 2.0 *) (3.0 4.0 +) /)")
    assert tokens == ["(", "(", "1.5", "2.0", "*", ")", "(", "3.0", "4.0", "+", ")", "/", ")"]

def teste_op_duplo():
    tokens = parseExpressao("(10 3 //)")
    assert tokens == ["(", "10", "3", "//", ")"]

def teste_variavel_mem():
    tokens = parseExpressao("(5.0 PRECO)")
    assert tokens == ["(", "5.0", "PRECO", ")"]

def teste_res():
    tokens = parseExpressao("(1 RES)")
    assert tokens == ["(", "1", "RES", ")"]

def teste_memoria_simples():
    tokens = parseExpressao("(TAXA)")
    assert tokens == ["(", "TAXA", ")"]

# Entradas inválidas

def teste_numero_duplo_ponto():
    try:
        parseExpressao("(3.14.5 2.0 +)")
        assert False
    except Exception:
        assert True

def teste_operador_invalido():
    try:
        parseExpressao("(3.0 2.0 &)")
        assert False
    except Exception:
        assert True

def rodar_testes():
    teste_exp_soma()
    teste_exp_aninhada()
    teste_op_duplo()
    teste_variavel_mem()
    teste_res()
    teste_memoria_simples()
    teste_numero_duplo_ponto()
    teste_operador_invalido()
    print("Todos os testes léxicos passaram")

if __name__ == "__main__":
    rodar_testes()