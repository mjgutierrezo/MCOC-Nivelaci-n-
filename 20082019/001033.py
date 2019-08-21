# Nivelación MCOC II. Funciones en Pyhton
"""
001033:
BMI calculator 
"""

from numpy import * #librería importada 

#datos perosna 1
name1 = "YK"
altura_m1 = 2
peso_kg1 = 90

#datos persona 2
name2 = "Hermana"
altura_m2 = 1.8
peso_kg2 = 70

#datos persona 3
name3 = "Hermano"
altura_m3 = 2.5
peso_kg3 = 160 

#calcular BMI para cada pesona para conocer si se encuantran en sobre peso o no 

def BMI(name, height_m, weight_kg): #función toma 3 argumentos
    bmi = weight_kg / (height_m ** 2) #fórmula para clacular bmi
    print ("BMI: ") # función como código
    print (bmi) #función como código
    if bmi < 25: #condición para saber si persona se encuentra en sobrepeso 
       return name + " is not overwieght" #lo que retorna al llamar la función como variable
    else: #si parámetros con cumplen con condición previa 
        return name + " is overwieght" #lo que retorna al llamar la función como variable 
        
# asignar parámetros de cada persona a la función
# los resultados que retornan los valores (nombre, peso, altura) se transmiten a las siguientes variables: 
result1 = BMI(name1, altura_m1, peso_kg1)  
result2 = BMI(name2, altura_m2, peso_kg2)  
result3 = BMI(name3, altura_m3, peso_kg3)

# si se deja el código hasta acá, la consola sólo ejecutará código de función, arrojando valor de bmi

#para saber si la persona esta en sobre peso, deben evaluarse las variables a las cuales se les asignó la función para cada individuo, de este modo saber que retorna "return" 
print result1
print result2
print result3

