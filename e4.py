"""
e4
29/11/23
"""
try:
    BLANCO = "██"
    NEGRO = "  "
    tablero = [[BLANCO if (i + j) % 2 == 0 else NEGRO for j in range(8)] for i in range(8)]
    for fila in tablero:
        print("".join(fila))
except ValueError:
    print("Valor invalid")
