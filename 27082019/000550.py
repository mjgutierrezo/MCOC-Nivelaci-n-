# -*- coding: utf-8 -*-
"""
editar fotos
"""

#ejemplo de como usar arreglos para modificar fotos
#000550

from skimage import io #librería para trsabajar con imágenes
import matplotlib.pyplot as plt #para mostrar imágen en consola

photo = io.imread("nombre archivo.jpg") #importar archivo desde documentos
#foto es tipo numpy.ndarray

print (photo.shape) #retorna dimenciones de foto (filas, columnas, )
plt.imshow(photo) #mostrar imágen en consola

#modificar foto
plt.imshow(photo[::-1]) #retorna imágen con filas invertidas
# imágen se muestra de cabeza

plt.imshow(photo[:, ::-1]) #retorna imágen con columnas invertidad
#se muestra foto espejo

plt.imshow(photo[50:150, 150:280]) #retorna sección especificada de la foto
#retorna una sección de la foto