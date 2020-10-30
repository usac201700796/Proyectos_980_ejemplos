import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# CON ESTO PODEMOS CAMBIARLE LA RESOLUCION A NUESTRA CAMARA
# PERO EL VALOR DE LA RESOLUCION DE LA CAMARA SOLO PUEDE TOMAR VALORES ENTRE EL RANGO DE LA CAMARA MISMA
# SI YO LE MANDO UN VALOR POR DEBAJO DEL VALOR MINIMMO AUTOMATICAMENTE TOMARA EL VALOR MINIMO
# IGUAL CON EL MAXIMO VALOR NO PUEDE PASARSE DE AHI
#cap.set(3, 3000)
#cap.set(4, 3000)

#print(cap.get(3))
#print(cap.get(4))


while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Whidth: '+ str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.line(frame, (0, 90), (400, 255), (147, 96, 44), 3)
        #frame = cv2.line(frame, (0, 0), (255, 255), (147, 96, 44), 3)
        frame = cv2.putText(frame, datet,  (10, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
