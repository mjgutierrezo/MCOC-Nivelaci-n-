# Nivelación MCOC I. If Else
"""
El bloque if y else son estructuras que permiten 
crear condiciones entre las variables del prograna, con el fin de
controlar la ejecución y flujo de este

000930: cuando se espera que el programa sea ejecutado según una condición se utiliza el bloque if, 
si además esperamos una respuesta cuando las variables no la cumplen se recurre a else, el cual retorna un resultados
para todos los casos que la condición planteada no abarque.
"""

from numpy import * #librería importada 

# primera paso: describir nuevas variables a utilizar 
c = 5
d = 4
if c < d: # definir la cindición inicial
    print ("c es menor a d") #retorna sólo cuando se cumpleala condición
#cuando queremos que el programa retorne algo sólo si no se cumplen las o la condición previamente establecidas, se usa el bloque else
else: #else debe ir fuera del bloque if, ya que aplica a los casos que no cumplen if
    print ("c no es menor a d ") 
    #asimismo la nosola puede retornar más de un print
    print ("se espera que c sea menor a d")
    #lo anterior se ejecuta sólo cuando else es válido
print ("fuera del bloque") #al no pertenecer a ningún bloque, comando se ejecuta 