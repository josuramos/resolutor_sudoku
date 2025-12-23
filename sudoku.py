# Sudoku
tablero = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        if i % 3 == 0 and i!=0:
            print("-" * 23)
        for j in range(len(tablero[0])):
            if j % 3 == 0 and j!=0:
                print(" | ", end="")
            if j == 8:
                print(tablero[i][j])
            else:
                print(f"{tablero[i][j]} ", end="")

def encontrar_vacio(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                return fila, col
    return None

def es_valido(tablero, num, fila, col):
    for j in range(9):
        if tablero[fila][j] == num and j!= col:
            return False

    for i in range(9):
        if tablero[i][col] == num and i!= fila:
            return False

    bloque_fila = (fila // 3) * 3
    bloque_col = (col // 3) * 3

    for i in range(bloque_fila, bloque_fila + 3):
        for j in range(bloque_col, bloque_col + 3):
            if tablero[i][j] == num and (i, j) !=  (fila, col):
                return False

    return True

def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True
    fila, col = vacio

    for num in range(1, 10):
        if es_valido(tablero, num, fila, col):
            tablero[fila][col] = num

            if resolver_sudoku(tablero):
                return True

            tablero[fila][col] = 0

    return False

if resolver_sudoku(tablero):
    imprimir_tablero(tablero)
else:
    print("No se pudo resolver el Sudoku.")
