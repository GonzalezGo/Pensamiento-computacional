def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))


def inicializar_tablero():
    tablero= [[' ' for _ in range(10)]for _ in range(10)]
    for i in range (10):
        for j in range(10):
            if (i + j) % 2 ==0:
                tablero[i][j] = '▉'
            else:
                tablero[i][j] = ' '
    return tablero

tablero= inicializar_tablero()
imprimir_tablero(tablero)