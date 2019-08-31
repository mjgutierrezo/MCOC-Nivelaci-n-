# Nivelación MCOC,
"""
operaciones numéricas en varias dimenciones (2)
"""
from matplotlib import pyplot as plt #importar librería

#001100
#graficar dos curvas en un nismo gráfico

x =[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] #lista identifica eje x
y1 = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752] # lista identifica eje y
y2 = [45372, 48876, 53850, 57287,63016,65998,70003,70000,71496,75370,83640] #adicion otra lista 

#comando para graficar
plt.plot(x, y1, color = "k", linestyle="--", marker = ".", label = "curva 1") #grafica lista x según y1
#grafica curva café punteada de x según y1,
#cada punto esta representado por un punto "."
 
plt.plot(x, y2, color = "b", marker ="o", label = "curva 2") #grafica lista x según y2
#grafica curva azul de x según y2
#cada punto esta representado por un círculo

#añadir título a ejes
plt.ylabel("Salario medio (USD)")
plt.xlabel("Edades")

#añadir título a gráfico 
plt.title("Salario promedio (USD) por edad")

#primer elemento de la lista hace referencia a primer comando de graficar
plt.tight_layout() #hace intersecciones entre curvas más exactas
plt.grid(True) #genera gráfico cuadriculado
plt.legend() #nombre a las curvas
#plt.safefig("plot.png") gráfico creado queda guardado como artículo png
plt.show()









