# Nivelación MCOC I. If Else
"""
El bloque if y else son estructuras que permiten 
crear condiciones entre las variables del prograna, con el fin de
controlar la ejecución y flujo de este

000627: el bloque if permite retornar información sólo si se cumple 
la condición establecida 
"""

from numpy import * #librería importada 

# primera paso: describir las variables a utilizar 
a = 1
b = 2
# queremos que el programa muestre cuando a es menor a b
if a < b: #se recurre a bloque if para que el programa muestre el resultado sólo si se cumple condición
    print ("a es menor a b") #solo retorna dicho mensaje si se cumple la condición a<b
    #print se encuentra dentro del bloque if
    print ("a es difinitivamente menor a b") #el bloque if puede tener más de un retorno
    #print dentro del bloque sólo se ejecutan si se cumple condición

print ("if se ejecuta según el valor otorgado por las variables") #print se encuentra fuera del bloque, por lo tanto, se ejecuta de todas formas, ya que no depende de la condición
