# Definimos la matriz 3x3
matriz = [
    [9, 2, 7],
    [4, 5, 6],
    [1, 8, 3]
]

# Elegimos la fila a ordenar
fila_a_ordenar = 1  # Por ejemplo, queremos ordenar la segunda fila

# Muestra la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Inicio del "QuickSort" simplificado para una fila específica
# Vamos a simular el proceso sin usar funciones

inicio = 0
fin = len(matriz[fila_a_ordenar]) - 1
pila = [(inicio, fin)]

while pila:
    pos = pila.pop()
    inicio, fin = pos[0], pos[1]
    pivote = matriz[fila_a_ordenar][inicio]

    i = inicio + 1
    j = fin

    while i <= j:
        while i <= j and matriz[fila_a_ordenar][i] <= pivote:
            i += 1
        while i <= j and matriz[fila_a_ordenar][j] >= pivote:
            j -= 1
        if i < j:
            # Intercambiamos los valores
            matriz[fila_a_ordenar][i], matriz[fila_a_ordenar][j] = matriz[fila_a_ordenar][j], matriz[fila_a_ordenar][i]

    # Colocamos el pivote en su lugar correcto
    matriz[fila_a_ordenar][inicio], matriz[fila_a_ordenar][j] = matriz[fila_a_ordenar][j], pivote

    # Añadimos los segmentos izquierdo y derecho a la pila
    if inicio < j-1:
        pila.append((inicio, j-1))
    if j+1 < fin:
        pila.append((j+1, fin))

# Muestra la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
