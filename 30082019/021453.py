# Nivelación MCOC,
"""
someter elementos dentro de arreglo a condiciones
"""
#005845
a = np.array([3, -1, -2, 4, -6, 8])
#encontrar todos los números negativos
print (a < 0)
#retorna arreglo con verdadoreo o falso según elementos de arreglo cumple condicion
negativos = a < 0
#se crea arreglo con condición de números negativos
print (negativos)
print (a[negativos]) #retorna arreglo a sólo con elementos verdaderos
print (a[a<0]) #otra forma rápida de escribirlo

#también se pueden usar condiciones para dar valores a elementos que la cumplan
a[a < 0] = 0 #números negativos reemplazados por ceros
print (a)

#se puede aplicar cualquier condición
#en vez de "and" se usa &, "or" |
n = (a > 3) & (a < 8) #condición a cumplir
print (n) #qué elementos cumplen condición
print (a[n]) #retorna únicamente elementos que estén dentro de intervalo

 #comparar dos arreglos
a = np.array([10, 1, 20])
b = np.array([2, 3, 20])
n = a > b #arreglo con condición a cumplir
print (n)
print (a[a > b]) #elemento que cumple condición

# en qué posición se cumple condición
print (np.nonzero(a > b)) #retorna índice donde es True