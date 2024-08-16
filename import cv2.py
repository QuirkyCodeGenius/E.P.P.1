import cv2
import numpy as np

# Abre la c�mara
cap = cv2.VideoCapture("/dev/video0")

if not cap.isOpened():
    print("No se puede abrir la c�mara")
    exit()

redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)
redBajo2 = np.array([175, 100, 20], np.uint8)
redAlto2 = np.array([179, 255, 255], np.uint8)
verdeBajo = np.array([50, 150, 20], np.uint8)
verdeAlto = np.array([80, 255, 255], np.uint8)

while True:
    ret, imagen = cap.read()
    if not ret:
        print("No se puede recibir el frame (fin del stream?). Saliendo ...")
        break

    imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    maskRED1 = cv2.inRange(imagenHSV, redBajo1, redAlto1)
    maskRED2 = cv2.inRange(imagenHSV, redBajo2, redAlto2)
    maskRED = cv2.add(maskRED1, maskRED2)
    maskVERDE = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
    maskRedvis = cv2.bitwise_and(imagen, imagen, mask=maskRED)
    maskVerdevis = cv2.bitwise_and(imagen, imagen, mask=maskVERDE)

    contornos_rojos, _ = cv2.findContours(maskRED, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos_verdes, _ = cv2.findContours(maskVERDE, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contornos_rojos:
        area = cv2.contourArea(c)
        if area > 10000:
            New1 = cv2.convexHull(c)
            epsilon = 0.0475 * cv2.arcLength(New1, True)
            approx = cv2.approxPolyDP(New1, epsilon, True)
            print(len(approx))
            cv2.drawContours(maskRedvis, [approx], 0, (0, 0, 255), 2)

    for D in contornos_verdes:
        area2 = cv2.contourArea(D)
        if area2 > 10000:
            New2 = cv2.convexHull(D)
            epsilon1 = 0.0475 * cv2.arcLength(New2, True)
            approx1 = cv2.approxPolyDP(New2, epsilon1, True)
            cv2.drawContours(maskVerdevis, [approx1], 0, (0, 255, 0), 2)

    deteccionColor = cv2.add(maskRedvis, maskVerdevis)

    cv2.imshow('deteccion de color', deteccionColor)
    cv2.imshow('video', imagen)

    if cv2.waitKey(1) == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()
