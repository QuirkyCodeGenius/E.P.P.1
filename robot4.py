#https://docs.python.org/fr/3/library/time.html
import time
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from roboticstoolbox import *
from spatialmath.base import *
import math
import numpy

l1 = 10
l2 = 10

# Cinemática inversa
#Px = 20 -7.012
#Py = 0  -9.543

Px = 20
Py = 0
b = math.sqrt(Px**2+Py**2)
# Theta 2
cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
theta2 = math.atan2(sen_theta2, cos_theta2)
print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
# Theta 1
alpha = math.atan2(Py,Px)
phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
theta1_x = alpha - phi
theta1 = round(theta1_x, 4)
#no esta entrando al if cuando seleccionamos el cuadrante negativo
x = -3.1416
if theta1 <= (x) :
    theta1 = ((2*math.pi) + theta1)


print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
#-------------
#convertir de radianes a grados
grado_servo1 = theta1 * (180/3.1416)
grado_servo2 = theta2 * (180/3.1416)

q1 = theta1
q2 = theta2




#Constants
nbPCAServo=2

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

 

    


# function pcaScenario 
def pcaScenario():

    angulo_deseado1 = grado_servo1
    angulo_deseado2 = grado_servo2

    if grado_servo1 == 0:
        angulo_deseado1 = 1
        
    if grado_servo2 == 0:
        angulo_deseado2 = 1
    if grado_servo1 == 0 and grado_servo2 == 0:
        angulo_deseado1 = 1
        angulo_deseado2 = 1

    
    
    angulo_final1 = (180 / angulo_deseado1) 
    angulo_final2 = (180 / angulo_deseado2) 
    
        
    pca.servo[0].angle = (MAX_ANG[0] / angulo_final1)
    pca.servo[1].angle = (MAX_ANG[0] / angulo_final2)

    #R = []
    #R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
    #R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

    
    #Robot = DHRobot(R, name='Bender')
    #print(Robot)

    #Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])
    #valor1, valor2 = Robot.teach([q1,q2]) 

    #zlim([-15,30]);

    #MTH = Robot.fkine([q1,q2])
    #print(MTH)
    #x =tr2rpy(MTH.R, 'deg', 'zyx')
    #print(f'Roll, Pitch, Yaw = {x}')

        

if __name__ == '__main__':
    init()
    main()
