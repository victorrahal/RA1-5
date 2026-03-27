# Função responsável por apresentar os resultados do código
def exibirResultados(resultados: list[float]) -> None:
    print("=" * 40)
    print("RESULTADOS DAS EXPRESSÕES")
    print("=" * 40)
    for i, resultado in enumerate(resultados):
        # Se o resultado é um inteiro exato, exibe sem casa decimal
        if resultado == int(resultado):
            print(f"  Linha {i + 1}: {int(resultado)}")
        else:
            print(f"  Linha {i + 1}: {resultado:.6f}")
    print("=" * 40)
    print(f"  Total de expressões processadas: {len(resultados)}")
    print("=" * 40)