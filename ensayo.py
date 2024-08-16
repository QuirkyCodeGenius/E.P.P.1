import time
import math
import numpy

from adafruit_servokit import ServoKit
from roboticstoolbox import *
from spatialmath.base import *

import time
from adafruit_servokit import ServoKit

# Constantes
nbPCAServo = 16
MIN_IMP = [500] * 16
MAX_IMP = [2500] * 16
MIN_ANG = [0] * 16
MAX_ANG = [180] * 16

# Objetos
pca = ServoKit(channels=nbPCAServo)

# Estado inicial de los ángulos de los servos
current_angle_servo1 = 0
current_angle_servo2 = 0

# Función para inicializar los rangos de ancho de pulso del servo
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i], MAX_IMP[i])

# Función principal
def main():
    init()
    pcaScenario(speed=0.1)  # Velocidad por defecto: 0.1

# Mover directamente los servos a las nuevas posiciones
def pcaScenario(speed):
    global current_angle_servo1, current_angle_servo2

    # Posiciones a recorrer
    #posiciones = [(0, 20), (-20, 0), (0, 20), (-20, 0)]
    posiciones = [(-0.056, 4.164),(0.403, 12.887),(-9.216, 13.661),(-10.148, 4.525)]
    #(-0.056, 4.164),(0.403, 12.887),(-9.216, 13.661),(-10.148, 4.525)
    
    # Número de pasos
    steps = 20

    for pos in posiciones:
        px, py = pos
        #px = ((1/5)*px1)-64.2
        #py = ((3/5)*py1)-4.2
        theta1, theta2 = calcular_angulos(px, py)
        grado_servo1 = theta1 * (180 / math.pi)
        grado_servo2 = theta2 * (180 / math.pi)

        # Calcular incremento angular para cada servo
        incremento_servo1 = (grado_servo1 - current_angle_servo1) / steps
        incremento_servo2 = (grado_servo2 - current_angle_servo2) / steps

        # Mover los servos hacia las posiciones calculadas
        for step in range(steps + 1):
            pca.servo[0].angle = current_angle_servo1 + step * incremento_servo1
            pca.servo[1].angle = current_angle_servo2 + step * incremento_servo2
            time.sleep(speed)

        # Actualizar los ángulos actuales
        current_angle_servo1 = grado_servo1
        current_angle_servo2 = grado_servo2

# Función para calcular los ángulos theta1 y theta2 a partir de las coordenadas x, y
def calcular_angulos(px, py):
    # Parámetros
    l1 = 10
    l2 = 10

    # Calcular b
    b = math.sqrt(px**2 + py**2)

    # Calcular theta2
    cos_theta2 = (b**2 - l1**2 - l2**2) / (2 * l1 * l2)
    sen_theta2 = math.sqrt(1 - cos_theta2**2)
    theta2 = math.atan2(sen_theta2, cos_theta2)

    # Calcular theta1
    alpha = math.atan2(py, px)
    phi = math.atan2(l2 * sen_theta2, l1 + l2 * cos_theta2)
    theta1 = alpha - phi

    return theta1, theta2

if __name__ == '__main__':
    main()
