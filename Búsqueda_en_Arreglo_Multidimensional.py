# Definimos la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor que queremos buscar
valor_buscado = 6

# Variable para determinar si encontramos el valor
encontrado = False

# Recorremos la matriz para buscar el valor
for i in range(3): # Recorre las filas
    for j in range(3): # Recorre las columnas
        if matriz[i][j] == valor_buscado:
            encontrado = True
            fila, columna = i, j
            break # Salimos del bucle interno si encontramos el valor
    if encontrado:
        break # Salimos del bucle externo si encontramos el valor

# Mostramos el resultado de la búsqueda
if encontrado:
    print(f"Valor encontrado en la posición: ({fila}, {columna})")
else:
    print("Valor no encontrado")
