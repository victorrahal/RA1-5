# Instituição
Pontifícia Universidade Católica do Paraná
## Disciplina
Linguagens Formais e Compiladores
### Professor
Frank Coelho de Alcantara
### Grupo
RA1-5
### Alunos
- João Henrique Tomaz Dutra - @Jhtomaz
- Lucas Balint Vilar        - @lucasdxl
- Paulo Henrique Eidi Mino  - @phmino
- Victor Rahal Basseto      - @victorrahal

## Sobre o projeto

Um programa em Python que lê expressões aritméticas em Notação Polonesa Inversa (RPN) de um arquivo de texto, realiza análise léxica usando Autômatos Finitos Determinísticos e gera código Assembly ARMv7 compatível com o simulador CPUlator (modelo DEC1-SOC v16.1).

### Operadores suportados

- | Operador | Descrição |
- | `+` `-` `*` `/` | Operações básicas com reais (64 bits IEEE 754) |
- | `//` | Divisão inteira |
- | `%` | Resto da divisão |
- | `^` | Potenciação (expoente inteiro positivo) |

### Comandos especiais

- `(N RES)` — retorna o resultado da expressão na posição N do histórico
- `(V MEM)` — armazena o valor V em uma memória de nome MEM
- `(MEM)` — retorna o valor armazenado em MEM (0.0 se não inicializada)

Expressões podem ser aninhadas sem limite, por exemplo: ((3.0 2.0 *) (4.0 2.0 +) /)

---

## Como executar

Dentro da pasta `src`:

bash
python main.py arquivo1.txt*

*arquivo1.txt pode ser substituido por arquivo2.txt ou arquivo3.txt

O programa imprime os tokens gerados, os resultados das expressões, e salva dois arquivos na pasta outputs/:

Assembly.s — código Assembly gerado
tokens.json — tokens da análise léxica

---

## Como testar

Dentro da pasta src:
python -m pytest ../teste/ -v

---

Estrutura

RA1-5/
- ├── outputs/
- │  ├── Assembly.s
- │  └── tokens.json
- ├── src/
- │   ├── main.py
- │   ├── parseExpressao.py
- │   ├── executarExpressao.py
- │   ├── gerarAssembly.py
- │   ├── exibirResultados.py
- │   ├── lerArquivo.py
- │   ├── utils.py
- │   ├── arquivo1.txt
- │   ├── arquivo2.txt
- │   └── arquivo3.txt
- └── teste/
-     ├── testeArquivo.py
-     ├── testeAssembly.py
-     ├── testeExec.py
-     ├── testeLexico.py
-     └── testeParse.py

---

## CPUlator

O arquivo outputs/Assembly.s pode ser carregado diretamente no CPUlator ARMv7 — selecione o modelo ARMv7 DEC1-SOC (v16.1).
