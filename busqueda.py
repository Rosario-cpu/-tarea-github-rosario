#Programa1: Busqueda en Arreglo Multidimensional
#Matriz 3*3 con valores numericos

matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [7, 1, 6]
]
#Funcion para buscar un valor en la matriz

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i,j)
    return None

#Valor que deseas buscar

valor_buscado =4

#Ejecutar la busqueda

resultado = buscar_valor(matriz, valor_buscado)

#Mostrar el resultado

if resultado:
    print(f"Valor {valor_buscado} encontrado en la posicion: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz.")
