import cv2
# ME ACTIVA LA CAMARA Y LA GUARDA EN UNA VARIABLE
# EL ARGUMENTO ME INDICA QUE CAMARA SE ACTIVA
cap = cv2.VideoCapture(0);
#EL ESTADO DE LA CAMARA, SI SE ACTIVA O NO
print(cap.isOpened())
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


while (True):
    #LEE LA CAMARA Y DEVUELVE VALORES TRUE O FALSE SI ESTA ACTIVADA  O NO
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        # CONVIERTE LA IMAGEN DE LA CAMARA EN ESCALA DE GRISES
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # MUESTRA LA VARIABLE EN UNA VENTANA
        cv2.imshow('frame', gray)
    # ESTO ES UN CONDICION PARA QUE LA CAMARA SE CIERRE AL PRESIONAR Q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#LIMPIA LA VARIABLE
cap.release()
out.release()
# CIERRA TODAS LAS VENTANAS
cv2.destroyAllWindows()
