# Nivelación MCOC II. Funciones en Pyhton
"""
001400:
"desafío"
crear una función que convierta millas en kilómetros

"""

from numpy import * #librería importada 

def convert(miles): #función que se le entrega argumento (millas) y debe pasarlas a Km
    km = 1.6 * miles #fórmula para pasar de millas a km
    return km #resultado de función

#llamar la función   
Km = convert(5) #variable que busca el valor de millas en km
print " equivalen a: ", Km, " Km" #para conocer resultado de función
