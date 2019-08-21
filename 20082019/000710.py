# Nivelación MCOC II. Funciones en Pyhton
"""
000810:
"Crear una función combinando el estilo mapeo con la serie de códigos"

"""

from numpy import * #librería importada 

def function4(x): #tomar argumento x
    print x
    print ("still in this function") #instrucciones de código 
    return 3*x #luego de realizar cídigo retornar un valor de argumento transformado
    
#llamar la función
f = function4(4) # al evaluar function4 en x=4, primero se ejecuta el código y luego se rtetornará el valor de la variable

print f # necesario si se quiere conocer valor que retorna función como return
   