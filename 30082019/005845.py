# Nivelación MCOC,
"""
operaciones numéricas en varias dimenciones (2)
"""
#020100
#operación verias dimensiones
a = np.array([[1, 2, 3], [4, 5, 6]])
print (a.sum()) #retorna suma de todos elementos 
#retorna 21

#suma vertical
print (a.sum(axis = 0)) #axis = 0 hace referencia a eje vertical
#retorna [5, 7, 9]

#suma horizontal (filas)
print (a.sum(axis = 1)) #axis = 1 hace referencia a filas
#retorna [[6], [15]]

#021030
a = np.arange(24).reshape(6, 4) #arreglo de 6 filas con 4 elementos cada uno (desde 0 a 23)
#obtener media para cada fila
#se usa función "mean"
print (a.mean(axis = 1)) #retorna arreglo con media en cada fila
print (a.mean(axis = 1).shape) #ina dimensión con 6 elementos 
