# Nivelación MCOC II. Funciones en Pyhton
"""
000710:
"Múltiples argumentos en una función "
Forma de mapeo de argumentos, retorna como variable
variable llama la función, entregándole valores a los respectivos argumentos 

"""

from numpy import * #librería importada 

def function3(x, y): #función toma dos argumentos (x, y) 
    return x + y # forma en que retorna los valores
    
#llamar la función
e = function3(1, 2) #variable e toma el valor correspondiente a la función, evaluando los argumentos (x, y) como (1, 2)
print e #para conocer resultado 
