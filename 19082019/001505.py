# Nivelación MCOC I. If Else
"""
El bloque if y else son estructuras que permiten 
crear condiciones entre las variables del prograna, con el fin de
controlar la ejecución y flujo de este

001505:para trabajar con varios casos (condiciones) sin usar elif
pueden crearse condiciones dentro de un bloque, las cuales se aplican sólo si el blonque dentro del cual estan es verdadero

"""

from numpy import * #librería importada 

# primera paso: describir nuevas variables a utilizar 
g = 7
h = 8

if g < h :#condición inicial
    print ("g es menor a h") #retorno si condición inicial es verdad

else: # se usa else si todo lo anterior no es verdad 
    if g == h: #nueva condición se encuentra dentro de else, por lo tanto si se cumple else, se aplica if
        print ("g es igual a h") # retorna sólo si variables cumplen con nueva condición 
    else: # de no ser ciertos los casos anteriores (dentro del bloque else), este bloque es verdad
        print ("g es mayor a h") #retorno correspondiente a nuevo bloque else 
    