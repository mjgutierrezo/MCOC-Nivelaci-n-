# Nivelación MCOC, "Arreglos en Numpy"
"""
Se demuestra porqué es conveniente usar Numpy en vez de listas python 
#1. no es necesario utilizar un bloque para implementar una fucnión a casa elemento dentro del arreglo
#2. se ejecuta más rápido al asegurarse que todos los elementos del arreglo son del mismo tipo
#3. usa menos memoria, por lo que ejecución es más lenta
"""
import numpy as np #importar librería

a = np.array([2, 3, 4]) #crear un arreglo con una lista dentro
b = np.arange(1, 12, 2) #crear un arreglo con elementos de dos en dos del 1 hasta 12
c = np.linspace(1, 12, 6) #crea un arreglo con 6 elementos desde el 1 hasta 12

print (b) #retorna [1, 3, 5, 7, 9, 11]
print (c) #retorna [1, 3.2, 5.4, 7.6, 9.8, 12]

#reformular un arreglo, dándole dos dimensiones
d = c.reshape(3, 2) #se crea un nuevo arreglo, el cual contiene arreglo "c" distribuido en tres filas con 2 elementos cada una
print (d) #matriz 3x2

#guardar modificación en arreglo
c = c.reshape(3,2)
print (c) #retorna "c" modificado

#conocer características de arreglo
print (c.size) #retorna cuántos elementos hay dentro del arreglo, no las dimensiones
print (c.shape) #retorna dimendiones de arreglo
print (c.dtype) #retorna tipo de variable que es "c"
print (c.itemsize) #cuánta memoria en byts cada elementos del arreglo usa 

#cómo funcionan paréntesis en un arreglo
b = np.array([(1.5, 2, 3), (4, 5, 6)]) #arreglo () contiene una lista [], con dos dimensiones ()
print (b) #retorna arreglo de dos dimensiones con 3 elementos cada uno

#comparar cada elemento de un arreglo bidimensional
print (c < 4) #retorna verdadero o flaso, según si cada elemento cumple condición

#multiplicar cada elemento de arreglo
print (c * 3)

#operaciones aplicadas a arreglos no se guardan a no ser que se ordene cambiar la variable
#modificar c
c = c * 3
print (c) #retorna arreglo modificado

#crear un arreglo vacío lleno de ceros
e = np,zeros((3, 4)) #arreglo tres dimensiones con 4 elementos cada una, lleno de ceros
print (e) #retona arreglo de ceros

#crear arreglo lleno de unos
f = np.ones((2, 3)) #arreglo bidimensional con 3 elementos cada uno (lleno de unos)
print (f)
f = np.ones(10) #arreglo de 1D, con 10 unos
print (f)

#crear arreglo con valores aleatorios
g = np.random.random((2, 3)) #arreglo aleatorio 2D (3 elem. aleatorios cada uno)
print (g) #al usar random.random retorna números entre cero y uno
g = np.set_printoptions(precision = 2, suppress = True)
# precicion indica número de decimales
# suppress para indicar si se quiere o no notación científica
print (g) #retorna nuevo arreglo aleatorio con dos decimales cada elemento

g = np.random.randint(0,10,5) # arreglo desde 0 a 10 incluido, 5 elementos 
print (g) #elemento 1D aleatorio

#aplicar funciones matemáticas a arreglos

#sumar elementos de un arreglo
h = g.sum() #variable que guarda suma de elementos dentro de arreglo
print (h) #retorna suma acumulada

#determinar mínimo elemento
h = g.min() #función aplicada a arreglo, asociada a variable "h"
print (h)#retorma mímino de arreglo

#valor máximo 
h = g.max()#función aplicada a arreglo, asociada a variable "h"
print (h) #retorna mayor elemento del arreglo

#otras funciones:
print (g.mean())
print (g.var()) #obterner varianza dentro de arreglo
print (g.std())#desviación estándar

a = np.random.randint(1, 10, 6)
print (a)
a = a.reshape(3, 2)
print (a)
#suma de cada fila 
h = a.sum(axis = 1) #con axis = 1 se indica que sume filas 
print (h)
h = a.sum(axis = 0) #axis = 0 indica que sume comunas 
print (h)

#se pueden importar archivos
#data = np.loadtxt("nombre archivo.txt",dtype = np.unit8, delimiter = ", ", skiprows = 1)
#delimiter indica cómo se separan elementos del archivo (en este caso por comas)
#skiprows para saltar líneas (se quiere saltar primera línea)
#print (data) #muestra archivo como arreglo


a = np.arange(10) #arreglo desde 1 a 9
print (a) #retorna arreglo creado
#arreglos con elementos desordenados:
np.random.shuffle(a)
print (a) #arreglo con elelemntos en orden aleatorio

#para retornar un elemento aleatorio de un arreglo
print(np.random.choice(a))





 