# Nivelación MCOC IV: For Loops
"""
000320:
Función range: permite definir un intervalo de números y trabajar con ellos. Este intervalo puede definir una lista y ser usada como tal
Intervalo range (x, y) va desde x hasta (y-1)

"""

#se quiere sumar un conjunto de números
#sumar 1, 2, 3, 4

#range(1, 5)  se usa para crear se un intervalo de números de 1 a 5 (sin incluir 5)
#útil para ahorrar el escribir una lista que contenga todos los números y así poder usar "for"

#ver lo que hay dentro de range
c = list(range(1, 5)) #se crea una lista desde 1 a 4 y se le asigna a variable "c"
print (c) #consola retorna lista creada

#lista creada con range puede ser recorrida con bloque "for"
for i in range(1, 5): #para cada uno de los elementos dentro del intervalor (1,5)
    print (i) #imprimir elemento "i"

#elementos dentro de range también puden ser usados en operaciones
# sumar elementos
total = 0 #suma acumulada de elementos de intervalo
for i in range (1,7):
    total += i #se suma elemento "i" a variable "total"

print (total) #imprime suma acumulada de intervalo
   
    