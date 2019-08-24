# Nivelación MCOC V. "Ciclo While"
"""
Mientras se cumpla una condición se ejecuta automáticamente ciclo "While"

"""
#000100
#sumar todos los números menores a 5

Total = 0 #variable que indica suma acumulada
j = 1 #variable a sumar

while j < 5: #condición a la cual se somete la variable j
#a diferencia del ciclo "if", while se ejecuta hasta que variable ya no cumpla condición establecida
    Total += j
    j += 1 #para que ciclo avance o se repita, la variable debe ir cambiando su valor 
    #al terminar el loop, se sigue con el resto del código
print (Total) #una vez terminado el bloque, la consola improme el resultado final 


    