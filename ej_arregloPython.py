#crear un arreglo
cars = ["Volvo","Ford","BMW"]
print(cars)

#acceder a un elemento del arreglo
x = cars[0]
print(x)

#modificar un elemento del arreglo
cars[0] = "Toyota"
print(cars)

#retorna el número de elementos de un arreglo
x = len(cars)
print(x)

#################################################################

#Ejercicio: Operaciones con arreglos en Python

#importar biblioteca numpy
import numpy as np
import random

# 1.- Crea un arreglo de una dimensión con los números del 1 al 10

arr = np.arange(1,11)
print(f"Arreglo original: {arr}\n")  #imprime [1 2 3 4 5 6 7 8 9 10]


# 2.- Suma 5 a cada elemento del arreglo
arr = arr + 5
print(f"Arreglo después de sumar 5: {arr}\n") #imprime [6 7 8 9 10 11 12 13 14 15]

# 3.- Multiplica cada elemento del arreglo por 3
arr = arr * 3
print(f"Arreglo después de multiplicar por 3: {arr}\n")

# 4. Suma todos los elementos del arreglo
suma = np.sum(arr)
print(f"Suma de todos los elementos del arreglo: {suma}\n") 

# 5. Calcular el promedio de los elementos del arreglo
promedio = np.mean(arr)
print(f"Promedio de los elementos del arreglo: {promedio}\n")

# 6. Encuentra el valor máximo y mínimo del arreglo
maximo = np.max(arr)
minimo = np.min(arr)
print(f"Valor máximo del arreglo: {maximo}\n")
print(f"Valor mínimo del arreglo: {minimo}\n")

# 7. Obtener un valor aleatorio del arreglo
valor_aleatorio = random.choice(arr)
print(f"El valor aleatorio del arreglo: {valor_aleatorio}\n")

# Usar where() para encontrar los índices donde el valor es mayor que 5
indices = np.where(arr > 5)
print(f"Índices donde el valor es mayor que 5: {indices}\n")

###########################################################################################
# S U E L D O S

#Crear un arreglo con los datos 400000, 760000, 1100000, 650000, 654980, 987300, 700450, 442300.
#Filtrar los sueldos que son superiores a 500000
#Calcular el promedio de los sueldos filtrados

sueldos = np.array([400000, 760000, 1100000, 650000, 654980, 987300,
700450, 442300])
#filtro
sueldos_filtrados = sueldos[sueldos>500000]
#promedio
promedio = np.mean(sueldos_filtrados)
print(f"El promedio de los sueldos superiores a 500000 es: {promedio}\n")

#########################################################################################

# 1.- Ordenar el arrreglo en orden ascendente
# 2.- Filtrar el arreglo para eliminar cualquier número qu sea menos a 10
# 3.- Calcular la suma de los números  restantes del arreglo

arr = np.array([25,2,18,9,14,3,30])
#ordenar
ordenado = np.sort(arr)
print(f"Arreglo ordenado: {ordenado}\n")
#filtrar
arreglo_filtrado = ordenado[ordenado>=10]
print(f"Arreglo filtrado {arreglo_filtrado}\n")
#suma
# Usar np.isin() para crear una máscara booleana que es True para los elementos de arr1 que están en arr2
mask = ~np.isin(ordenado,arreglo_filtrado)
restante = ordenado[mask]
print(f"restante: {restante}\n")
suma = np.sum(restante)
print(f"la suma de los valores restantes es: {suma}")

#ordenar inversamente el arreglo ordenado
arreglo_inverso = ordenado[::-1]
print(f"inverso 1 {arreglo_inverso}")
#ordenar inversamente creando una lista
lista_inverso = list(reversed(ordenado))
print(f"inverso 2 {lista_inverso}")

#anexar un arreglo a otro arreglo

arr1 = [1,2,3]
arr2 = [4,5,6]
arr1.append(arr2)
print(arr1)  #imptime: [1, 2, 3, [4, 5, 6]]

arr1 = [1,2,3]
arr2 = [4,5,6]
arr1 += arr2
print(arr1) # Imprime: [1, 2, 3, 4, 5, 6]



