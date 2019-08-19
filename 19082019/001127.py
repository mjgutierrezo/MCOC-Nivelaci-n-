# Nivelación MCOC I. If Else
"""
El bloque if y else son estructuras que permiten 
crear condiciones entre las variables del prograna, con el fin de
controlar la ejecución y flujo de este

001127: Las variables son sometidas a una nueva condición gracias al bloque elif, el cual sólo se ejecuta 
si estas no cumplen con la condición del bloque if anterior. El bloque else retorna algo sólo si las variables no
cumplen con los requisitos de if y elif (no son verdad).
"""

from numpy import * #librería importada 

# primera paso: describir nuevas variables a utilizar 
e = 7
f = 8
if e < f: #condición inicial
    print ("e es menor a f") #lo que retorna si se cumple condición
    
# sólo si if no se cumple, se quiere que el programa someta a las variables a una nueva condición
elif e == f:#si if no se cumple, se chequea una nueva condición con elif
    print ("e es igual a f") #lo que retorna de sólo cumplirse elif
    
elif e > f + 10:#actúa como un "sino" para todas las condiciones anteriores
    print ("e es mayor a f más 10") #retorna sólo si bloques anteriores son falsos y este verdadero
    
else: #si no se cumple ninguna condición previamente establecida
   print("e es mayor a f") #retorna
   