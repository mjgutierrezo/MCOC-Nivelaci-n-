# Nivelación MCOC III. Listas

"000550: Aplicar lo aprendido, se pide intercambiar el primer elemento de la lista con el último"

#asignar a variable una lista definida 
b = ["banana", "apple", "microsoft"]
print b #se muestra lista original

primer_elemento = b[0] #se asigna a una variable el valor del primer elemento de la lista
b[0] = b[2] #primer elemento posee igual valor que el último (ambos ason microsoft)
b[2] = primer_elemento  # ahora el último elemento es reemplazado por el valor que inicialemtne tenía el primero

print (b) #consola retorna lista modificada 

#otra forma de hacerlo
b[0], b[2] = b[2], b[0] # se da instrucción de que cambie los valores de los índices 
print (b) #se muestran pindices invertidos, por lo que la lista vuelve a original 