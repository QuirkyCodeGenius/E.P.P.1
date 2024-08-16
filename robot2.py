#https://docs.python.org/fr/3/library/time.html
import time
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from roboticstoolbox import *
from spatialmath.base import *
import math

#Constants
nbPCAServo=16 

ServoKit.frequency = 50
#Parameters
MIN_IMP  =[500] * 16
MAX_IMP  =[2500] * 16
MIN_ANG  =[0] 
MAX_ANG  =[180]

#Objects
pca = ServoKit(channels=16)

# function init 
def init():

    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])


# function main 
def main():

    pcaScenario();

def grados():
    angulo_deseado = 90
    angulo_final = (MAX_ANG[180] / angulo_deseado) 

    


# function pcaScenario 
def pcaScenario():
     angulo_deseado = 180
     angulo_final = (180 / angulo_deseado) 

     angulo_deseado1 = 180
     angulo_final1 = (180 / angulo_deseado1) 
     
     angulo_deseado2 = 1
     angulo_final2 = (180 / angulo_deseado2) 
     while True:  # Bucle infinito para que la acción se repita continuamente.
        
        pca.servo[0].angle = (MAX_ANG[0] / angulo_final)
        pca.servo[1].angle = (MAX_ANG[0] / angulo_final1)
        pca.servo[2].angle = (MAX_ANG[0] / angulo_final2)
        #time.sleep(1)

if __name__ == '__main__':
    init()
    main()

############################################