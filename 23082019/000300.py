# -*- coding: utf-8 -*-
"""
Aplicar ciclo while para recorrer una lista y someter a los elementos dentro de ella a condiciones

"""
from numpy import *

#000300

given_list = [5, 4, 4, 3, 1, -2, -3, -5]
#se quiere obtener la suma de sólo los números positivos de la lista

total = 0
i = 0

# en vez de usar un ciclo for que evalúe cada uno de los elementos de la lista, se crea una condición para ellos con loop while
while i < len(given_list) and given_list[i] > 0:
    total += given_list[i] #suma acumulada
    i += 1 #modificar variable estudiada en el ciclo para continuar 
print (total) #retorna la suma total de elementos que cumplían condición    

#000740
#ejecutar ejercicio anterior con ciclo for 

total2 = 0

for element in given_list: #recorrer todos los elementos de la lista
    if element <= 0: #condición para evaluar números negativos dentro de lista
        break #se rompe ciclo if, continúa con for
    total2 += element #suma acumulada
print (total2) #retorna total de suma

#"break" también puede ser usado en ciclios while