# Nivelación MCOC,
"""
cómo obtener las características dimensionales, tipo de elementos, y menmoria que ocupa un arreglo
"""
#001900
a = np.array([1, 2, 3, 4]) #se coloca cada lista como arreglo con np.array()
b = np.array([10., 11., 12., 13.])
#los arreglos son mutables, se puede cambiar y añadir contenido
#ejemplo:
print (a[0]) #llamar primer elementos de lista "a"
#se quiere cambiar ese valor
a[0] = 10 #primer elemento tomará valor 10
print (a) #nuevo arreglo con primer elemento modificado

#cuando un arreglo tiene un dtype, si se quiere agregar un elemento numérico que no pertenece, este será modificado para que pertenezca al grupo del arreglo
#ejemplo:
print (a.dtype) #arreglo "a" es int32
a[0] = 10.45 #se quiere agregar un float
print ("10.45 es un elementos tipo ", type(10.45))
print (a) #nuevo arreglo modifica 10.45, dejándolo como 10 para que pertenezca a int32

#se puede imponer qué tipo de elementos debe contener el arreglo
a = np.array([1, 2, 3, 4.0], dtype = "int32") #aunque arreglo tenfa un elem float, todos se transforman a int32
print (a.dtype) #arreglo tipo int32


#002400
#dimensiones
c = np.array([[10, 11, 12], [20, 21, 22]]) #arreglo contiene una lista de listas (2 dimensiones = dos listas)
print (c) #retorna arreglo con dos filas y tres columnas (3 elementos en cada fila)
print (c.ndim) #arreglo creado de dos dimensiones
print (c.shape) #forma (2 filas, 3 columnas)
# (2, 3) indice[0] hace referencia a filas, indice [1] hace referencia a columnas o cantidad de elementos dentro de filas 

#no confundir arreglos de varias dimensiones con matrices

#arrelo traspuesto
print (c.T)

#cantidad de elementos dentro de arreglo 
print (c.size) #retona 6

#arreglos de varias dimensiones también pueden modificarse
#c[0,0] indica que se llama al primer elemento de primera fila 
print (c[0,0]) #retorna 10
#listas en python funcionan como c[0][0]

print (c[0]) #retorna primera fila 

#003338
#seleccionar sección del arreglo
a = array([10, 11, 12, 13, 14])
#se quiere seleccionar elementos 11 y 12
#11 usa índice 1 o -4
#12 usa índice 2 o -3

#formas de llamar parte del arreglo

print (a[1:3]) #retorna desde posición 1 a posición (3-1)
print (a[1:-2]) #retorna desde 1 hasta -3
print (a[-4:3]) #retorna desde -4 hasta 2

#retornas lo sprmeros tres elementos
print (a[0:3])
print (a[:3])

#retornar los últimos 2 elementos
print (a[-2:])

#retornar totos los elementos menos uno
print (a[::2]) #arreglo que incluye desde el primer al último elementos, pero de dos en dos 

#aplicado en dos dimensiones
c = np.array([[10, 11, 12, 13], [20, 21, 22, 23], [1, 2, 3, 4]]) #arreglo contiene una lista de listas (2 dimensiones = dos listas)
#obtener una sección de una fila 
print (c[0, 1:3])
#retorna elementos 1 y 2 de la primera fila (0)

#retornar una sección de dos o más dimensiones
print (c[1:3, 1:3]) 
#retorna arreglo desde la segunda a tercera fila, cuyos elementos ocupan índices 1 y 2

#retornar un elementos de cada fila
print (c[:, 1])  #retorna en forma de arreglo iD
#de cada fila se obtiene el elementos que usa índice 1

#saltándose elementos
print (c[::2, 1::2]) 
#de filas a usar selemcciona la primera y luego continúa de dos en dos
#de elementos dentro de filas seleccionas, comienza desde índice 1 y luego selecciona de dos en dos


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


#005845
a = np.array([3, -1, -2, 4, -6, 8])
#encontrar todos los números negativos
print (a < 0)
#retorna arreglo con verdadoreo o falso según elementos de arreglo cumple condicion
negativos = a < 0
#se crea arreglo con condición de números negativos
print (negativos)
print (a[negativos]) #retorna arreglo a sólo con elementos verdaderos
print (a[a<0]) #otra forma rápida de escribirlo

#también se pueden usar condiciones para dar valores a elementos que la cumplan
a[a < 0] = 0 #números negativos reemplazados por ceros
print (a)

#se puede aplicar cualquier condición
#en vez de "and" se usa &, "or" |
n = (a > 3) & (a < 8) #condición a cumplir
print (n) #qué elementos cumplen condición
print (a[n]) #retorna únicamente elementos que estén dentro de intervalo

 #comparar dos arreglos
a = np.array([10, 1, 20])
b = np.array([2, 3, 20])
n = a > b #arreglo con condición a cumplir
print (n)
print (a[a > b]) #elemento que cumple condición

# en qué posición se cumple condición
print (np.nonzero(a > b)) #retorna índice donde es True

#014313
#Arreglos multi- Dimensionales
# 1D, (x) arreglo horizontal (filas)
# 2D, (y, x) filas y columnas, elementos en dirección vertical y horizontal
# 3D, (z, y, x) arreglo con profundidad
# 4D, (w, z, y, x) w indica cuántas veces se repite arreglo 

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





