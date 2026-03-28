import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from gerarAssembly import gerarAssembly

def teste_ass_soma():
    tokens = [["(", "3.0", "2.0", "+", ")"]]
    resultado = gerarAssembly(tokens, arquivoSaida=os.devnull)
    assembly = "\n".join(resultado)
    assert "VADD.F64" in assembly

def teste_ass_subtracao():
    tokens = [["(", "5.0", "3.0", "-", ")"]]
    resultado = gerarAssembly(tokens, arquivoSaida=os.devnull)
    assembly = "\n".join(resultado)
    assert "VSUB.F64" in assembly

def teste_ass_multiplica():
    tokens = [["(", "4.0", "2.0", "*", ")"]]
    resultado = gerarAssembly(tokens, arquivoSaida=os.devnull)
    assembly = "\n".join(resultado)
    assert "VMUL.F64" in assembly

def teste_ass_divisao():
    tokens = [["(", "8.0", "2.0", "/", ")"]]
    resultado = gerarAssembly(tokens, arquivoSaida=os.devnull)
    assembly = "\n".join(resultado)
    assert "VDIV.F64" in assembly

def teste_ass_divisao_inteira():
    tokens = [["(", "7", "2", "//", ")"]]
    resultado = gerarAssembly(tokens, arquivoSaida=os.devnull)
    assembly = "\n".join(resultado)
    assert "VCVT.S32.F64" in assembly

def teste_ass_potencia():
    tokens = [["(", "2.0", "3", "^", ")"]]
    resultado = gerarAssembly(tokens, arquivoSaida=os.devnull)
    assembly = "\n".join(resultado)
    assert "pot_" in assembly

def teste_ass_mem():
    tokens = [["(", "5.0", "VALOR", ")"]]
    resultado = gerarAssembly(tokens, arquivoSaida=os.devnull)
    assembly = "\n".join(resultado)
    assert "memo_VALOR" in assembly

def teste_ass_cabecalho():
    tokens = [["(", "1.0", "2.0", "+", ")"]]
    resultado = gerarAssembly(tokens, arquivoSaida=os.devnull)
    assembly = "\n".join(resultado)
    assert ".global _start" in assembly
    assert ".data" in assembly
    assert "_start:" in assembly

def rodar_testes():
    teste_ass_soma()
    teste_ass_subtracao()
    teste_ass_multiplica()
    teste_ass_divisao()
    teste_ass_divisao_inteira()
    teste_ass_potencia()
    teste_ass_mem()
    teste_ass_cabecalho()
    print("Todos os testes de Assembly passaram")

if __name__ == "__main__":
    rodar_testes()