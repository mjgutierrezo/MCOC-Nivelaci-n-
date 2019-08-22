# Nivelación MCOC IV: For Loops
"""
000014:
Como recorrer los elelmentos dentro de una lista uno por uno de forma automática
Gracias a bloque for estos elementos pueden ser sometidos a operaciones 

"""

a = ["banana", "apple", "microsoft"] #definir lista y otorgársela a variable "a"

#se quiere operar en cada uno de los elementos de la lista

#para imprimir en consola cada elemento
print (a[0])
print (a[1])
print (a[2])
#se debe especificar que imprima cada uno de los ítems de la lista

#para trabajar con listas grandes o ahorrar tiempo se usa "for loops"
for element in a: #bloque que recorre cada elemento de lista "a" 
    #para cada elemento ejecutar comando bajo el bloque 
    print (element) # se imprimirá cada elemento
    # se pueden agregar múltiples instrucciones bajo el bloque for
    print (element)

# la instrucción dada por bloque for se ejecuta para cada elemento, una vez terminada instrucción para elemento i pasa al siguiente

