# Nivelación MCOC I. If Else
"""
El bloque if y else son estructuras que permiten 
crear condiciones entre las variables del prograna, con el fin de
controlar la ejecución y flujo de este

001715: crear calculadora bmi "índice de masa corporal" (aplicar lo aprendido)
"""

from numpy import * #librería importada 

# primera paso: describir nuevas variables a utilizar 
name = "YK" #nombre de la persona que se evaluará
altura_m = 2 #altura de la persona 
peso_kg = 90 # peso de la persona en kg

#fórmula para calcular el bmi de una persona
bmi = peso_kg / (altura_m ** 2)
print ("bmi:") 
print (bmi) #retorno función bmi de la persona ingresada

#evaluar el bmi
if bmi < 25: #condición inicial para el bmi obtenido 
    print(name) #retona variable que llama
    print("no tiene sobrepeso") #si condición se cumple la persona tine esobrepeso

else: #si no se cumplen condiciones previas 
    print (name) #retorna nombre 
    print ("tiene sobrepeso") 
    