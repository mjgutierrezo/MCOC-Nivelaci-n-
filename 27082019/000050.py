# Nivelación MCOC, "Numpy"
"""
Librería numérica en Python
000516
Crear arreglos tipo float a partir de librería y bloques np
"""
import numpy as np #importar librería

#tener acceso a elementos dentro de un arreglo
z1 = np.random.randint(10, size = 6) #definir arreglo a utilizar
print (z1) #retorna arreglo aleatorio

print (z1[0]) #llamar primer elemento de la lista 
print (z1[0:2]) #retorna primer y segundo elemento de arreglo (2-1)
print (z1[-1]) #llamar al último elemento de arreglo


#000802
#aplicar funciones matemáticas a un arreglo
#se usará arreglo z1
#se quiere aplicar una función a todos los elementos dentro de la foto

z1_sin = np.sin(z1) #aplicar función seno a arreglo
print (z1_sin) #retorna arreglo modificado por función
