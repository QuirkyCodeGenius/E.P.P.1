import cv2

# Cargar la imagen
imagen = cv2.imread('/home/juliapaez1227/Documents/taller2corte/chevrolet.png')

# Verificar si la imagen ha sido cargada correctamente
if imagen is None:
    print("Error: La imagen no se pudo cargar. Verifica la ruta del archivo.")
else:
    # Mostrar la imagen
    cv2.imshow('Imagen Cargada', imagen)
    cv2.waitKey(0)  # Espera hasta que se presione una tecla
    cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas
