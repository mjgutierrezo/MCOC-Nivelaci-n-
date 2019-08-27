# Nivelación MCOC "Diccionarios"
"""
forma de guardar y trabajar con pares de datos Keys -Values

"""
#000350

d = {"George": 24, "Tom": 32, "Jenny": 16} #diccionario asociado a variable d
#variables pueden ser cualquier tipo mientras que keys son comunmente números y strings
#se pueden mezclar tipos de Keys

d[10] = 100 #agregar par k-v, ambos tipo número 
print (d[10]) #key y valor son números 

#iterar en un par key-value de un diccionario
for key, value in d.iteritems():#bloque para recorrer cada una de los pares k-v de un diccionario
    print ("key") 
    print (key)#retorna key correspondiente 
    print ("value")
    print (value) #retorna valor asociado a key llamada 
    print ("") #separa entre k-v 
    