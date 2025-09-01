#Programa 2: Ordenacion de una fila en matriz 3*3

matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [7, 1, 6],
]

# Fila que deseo ordenar (por ejemplo, la fila 1)

fila_original = matriz[1]
fila_ordenada = sorted(fila_original)
matriz[1] = fila_ordenada

print("Matriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)
