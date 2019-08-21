# Nivelación MCOC II. Funciones en Pyhton
"""
000505:

"""

from numpy import * #librería importada 
#ejemplo función como mapeo

def function2(x): # se define una función con nombre function2, la cual usará como input cualquier valor que se quiera estudiar (#)
    return 2*x #el resultado de la función (lo que retorna)
    #operación a la cual la función somete a input x

#llamar la función:
a = function2(3) # se le asigna a una variable el valor de la función, usando el parámetro que se quiere estudiar (3)
# 3 toma valor de x
print a #que consola retorne valor de función aplicada

b = function2(4) #podemos asignar el valor de la función a multiples varialbles, usando el input que nos interese
print b

c = function2(5)
print c
