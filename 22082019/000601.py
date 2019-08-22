# Nivelación MCOC IV: For Loops
"""
000600: 
Operaciones con algunos elementos de la lista o intervalo 
"""
#ejemplo 1
#encontrar suma de los números múltoplis de 3
print ("Ejemplo 1: ")

#definir una lista que contenga un intervalo de números
print (list(range(1, 8))) #consola muestra lista con que se trabajará

Total = 0 #variable de suma acumulada entre elem. múltiplos de 3

for i in range(1, 8):#bloque "for" que recorre intervalo
    if (i % 3) == 0:#condición de que elemento i sea múltiplo de tres
        Total += i #si condición es verdad, se suma a "Total"
        
print (Total)

#ejemplo 2
#suma de todos los múltiplo de 3 y 5 menosres a 100

print ("ejemplo 2: ")

numeros = list(range(1, 100))#definir intervalo con todos los números menores a 100
#print (numeros) #para mostrar lista en consola 

suma = 0 #variable de suma acumulada 

#ver que números son múltiplos de 3 y 5
for j in numeros : #recorres cada uno de los componentes de la lista
    if (j % 3) == 0 or ((j % 5) == 0): #establecer condición "si elementos son múltiplo de 3 o de 5"
        suma += j #si condición (bloque if) es verdadesra, sumar a variable "suma"

print (suma)
    
