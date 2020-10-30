import cv2
import numpy as np

#img = cv2.imread('lena.jpg', 1)
# CREAR UNA IMAGEN VACIA CON NUMPY
img = np.zeros([512, 512, 3], np.uint8)
# EL ARGUMENTO COLOR ESTA ORDENADO POR AZUL VERDE Y ROJO
# PARA VER EL CODGIO DE COLORES PUEDO BUSCAR RGB COLOR PICKER
img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 3)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (147, 96, 44), 3)
# EL PONER -1 EN TICKNEES ME RELLENA EL RECTANGUO
# PRIMER PUNTO ES EL VERTICE SUPERIOR
# SEGUNDO PUNTO ES EL VERTICE INFERIOR
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 1)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
# PONER TEXTO EN UNA IMAGEN
img = cv2.putText(img, 'Hola', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
