# Nivelación MCOC,
"""
obtener y modificar elementos o secciones dentro de un arreglo
"""
#021453
#mínimo y máximo
a = np.array([[1, 2, 3], [4, 5, 6]])

#encontrar mínimo para cada fila
print (a.min(axis = 1)) #arreglo de 1D [1, 4]
print (np.min(a, axis = 1)) #otra notación
#encontrar mínimo para cada columna
print (a.min(axis = 0)) #arreglo 1D [1, 2, 3]


#encontrar máximo en cada fila
print (a.max(axis = 1)) #arreglo 1D con máximos
print (np.max(a, axis = 1)) #otra notación
#encontrar máximo en cada columna
print (a.max(axis = 0)) #arreglo con máximos para cada columna


#dónde se encuentra el mínimo del arreglo
#usar comando "argmin"
b = np.array([2, 3, 0, 1])
print (b.argmin(axis = 0)) #retorna índice para columnas
print (np.argmin(b, axis = 0)) #notación como función
#retornan índice 2 (0)

#donde se encuentra el máximo del arreglo
#se usa comando "argmax"
print (b.argmax(axis = 0)) #retorna índice para columnas
print (np.argmax(b, axis = 0)) #notación como función
#retornan índice 1 (3)

#ejemplo propuesto
a = np.arange(-15, 15).reshape(5, 6)**2 #elementos de arreglo se elevan en 2
print (a)

#máximo para cada fila
print (a.max(axis = 1))
#media para cada columna
print (a.mean(axis = 0))

#posición de elemento menor

c = a.argmin(axis = 1) #lista de índices de elementos menor en cada fila
print (c) #posición del menor en cada fila
b = a.min(axis = 1) 
print b.argmin(axis = 0) #índice mínimo de mínimos
#posición
print (b.argmin(axis = 0), c[b.argmin(axis = 0)])






