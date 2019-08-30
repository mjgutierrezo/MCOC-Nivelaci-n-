# Nivelación MCOC, "Tutorial Numpy"
"""
arreglo de varias dimensiones 
crearlo, aplicar funciones y odificarlo
"""
import numpy as np #importar librería

#004232

#crear arreglo de varias dimensiones sin insertar listas
a = np.arange(25).reshape(5, 5)
#se crea un arreglo desde el cero a 25, luego se indica que debe ordenarse en 5 filas de 5 elementos cada una 
print (a) #retorna arreglo de 5 dimesniones 

#seleccionar secciones dentro de arreglo

#elementos índice 1 y 3 para todas las filas
print (a[:, 1::2])
#selecciona todas las filas
#para cada fila se toma desde el segundo elemento (1) de dos en dos 

#seleccionas elementos dispersos
print (a[1::2, :3:2]) 
#selecciona sefunda y cuarta fila
#selecciona primer elementos y luego el tercero

#seleccionar última fila
print (a[-1, :])

#estas secciones se pueden transformar en arreglos y ser modificados
r = a[:, 1::2]
b = a[1::2, :3:2]
y = a[-1, :]

#cambiar último elementos de r
r[-1, -1] = 0 #el último elementos de última fila es cero
print (r) #arreglo r modificado

print (a) #retorna arreglo a
#al modificar r (sección de "a") también se modificar el arreglo original
#para evitar eso para el resto de los arreglo (b, y) debe aplicarse comando.copy()

b.copy()
y.copy()

#modificar b
b[-1, -1] = 0
print b #arreglo b modificado
print a #arreglo a sin sufrir cambios de b

#005700
#crear arreglo a partir de otro

a = np.arange(0, 80, 10) #arreglo con números de 10 en 10, desde 0 hasto 80
indices = [1, 2, -3] #lista con índice que se quieren usar
n = a[indices] #y es un arreglo que contiene elementos en índices 1, 2, -3 del arreglo "a"
print (n) #ver arreglo creado




#014313
#Arreglos multi- Dimensionales
# 1D, (x) arreglo horizontal (filas)
# 2D, (y, x) filas y columnas, elementos en dirección vertical y horizontal
# 3D, (z, y, x) arreglo con profundidad
# 4D, (w, z, y, x) w indica cuántas veces se repite arreglo 


