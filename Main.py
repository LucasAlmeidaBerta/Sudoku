def checar_numero_linha(sudoku, linha, numero):
    inicio_linha = (linha - 1) * 9
    fim_linha = inicio_linha + 9
    linha_atual = sudoku[inicio_linha:fim_linha]
    return str(numero) in linha_atual


def checar_numero_coluna(sudoku, coluna, numero):
    for i in range(9):
        posicao = coluna - 1 + i * 9
        if sudoku[posicao] == str(numero):
            return True
    return False


def checar_numero_quadrante(sudoku, linha, coluna, numero):
    inicio_linha_quadrante = (linha - 1) // 3 * 3
    inicio_coluna_quadrante = (coluna - 1) // 3 * 3
    for i in range(3):
        for j in range(3):
            posicao = (inicio_linha_quadrante + i) * 9 + (inicio_coluna_quadrante + j)
            if sudoku[posicao] == str(numero):
                return True
    return False


def resolver_sudoku(sudoku):
    for pos in range(len(sudoku)):
        if sudoku[pos] == "0":
            linha = (pos // 9) + 1
            coluna = (pos % 9) + 1

            for tentativa in range(1, 10):
                if (not checar_numero_linha(sudoku, linha, tentativa) and
                        not checar_numero_coluna(sudoku, coluna, tentativa) and
                        not checar_numero_quadrante(sudoku, linha, coluna, tentativa)):

                    sudoku[pos] = str(tentativa)

                    if resolver_sudoku(sudoku):
                        return True

                    sudoku[pos] = "0"

            return False

    return True


def resolver_multiplo_sudoku(quantidade_sudokus, entrada_sudokus):
    dados = entrada_sudokus.split()
    index = 0
    resultados = []
    for _ in range(quantidade_sudokus):
        sudoku = dados[index:index + 81]
        index += 81

        resolver_sudoku(sudoku)

        resultados.append(" ".join(sudoku))

    return resultados


def capturar_entrada_multiplas_linhas():
    quantidade_sudokus = int(input("Digite a quantidade de Sudokus: "))
    entrada_sudokus = []
    for _ in range(quantidade_sudokus * 9):
        entrada_sudokus.append(input())
    return quantidade_sudokus, " ".join(entrada_sudokus)


quantidade_sudokus, entrada_sudokus = capturar_entrada_multiplas_linhas()
resultados = resolver_multiplo_sudoku(quantidade_sudokus, entrada_sudokus)
for resultado in resultados:
    print(resultado)
