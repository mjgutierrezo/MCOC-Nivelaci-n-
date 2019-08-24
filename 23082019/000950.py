# -*- coding: utf-8 -*-
"""
Aplicar "break" a ciclo while
"""
#000950

#ver cómo se aplica break a while

given_list = [5, 4, 4, 3, 1, -2, -3, -5]
#sumar elementos positivos de lista 

Total = 0
j = 0 #index a utilizar en while

while True: #condición que siempre será verdadera, simepre se ejecuta while
    Total += given_list[j] #suma acumulada
    j += 1
    if given_list[j] <= 0: #si elemento es negativo se rompe el ciclo
        break #continuar con el resto del código
        
print (Total) #resultado en consola 