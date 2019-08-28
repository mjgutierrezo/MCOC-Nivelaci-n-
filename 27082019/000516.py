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


