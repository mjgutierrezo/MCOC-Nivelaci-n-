# -*- coding: utf-8 -*-
"""
Ejercicio propuesto
"""
from numpy import *

#001224

given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

#se quiere obtener la suma de sólo los números negativos de la lista

total = 0
i = 0

while i < len(given_list): #primera condición: que el índice pertenezca a la lista
    if given_list[i] < 0: #que elemento sea negativo
        total += given_list[i] #suma acumulada
    i += 1 #modificar variable estudiada en el ciclo para continuar 
print (total) #retorna la suma total de elementos que cumplían condición    

