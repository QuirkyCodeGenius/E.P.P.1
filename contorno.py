import time
from adafruit_servokit import ServoKit    # Importa la biblioteca para controlar los servomotores

# Constants
nbPCAServo = 16 
# Parameters
MIN_IMP  = [500] * 16
MAX_IMP  = [2500] * 16
MIN_ANG  = [0] * 16
MAX_ANG  = [180] * 16

# Objects
pca = ServoKit(channels=nbPCAServo)

# Initialize servo pulse width range
def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i], MAX_IMP[i])

# Main function to control the movement of two servos
def main():
    pcaScenario()

# Incrementally move two servomotors
def pcaScenario():
    # Define initial and final angles
    position =[(0,0),(0,0),(0,90),(90,180),(180,180),(180,180)]
    position1 = [(0,150),(150,0),(0,0),(0,0),(0,90),(90,150)]


    # Define the number of steps
    steps = 40
    delay = 0.1  # Delay in seconds between each step

    for pos, pos1 in zip(position, position1):
        initial_angle, final_angle = pos
        initial_angle1, final_angle1 = pos1
        increment = (final_angle - initial_angle)/steps
        increment1 = (final_angle1 - initial_angle1)/steps

        for step in range(steps + 1):
            current_angle = initial_angle + step * increment
            pca.servo[0].angle = current_angle
            current_angle1 = initial_angle1 + step * increment1
            pca.servo[1].angle = current_angle1
            time.sleep(delay)
    

    # Move servomotors incrementally
    #for step in range(steps + 1):
      #  current_angle = initial_angle + step * increment
       # pca.servo[0].angle = current_angle
      #  current_angle1 = initial_angle1 + step * increment1
     #   pca.servo[1].angle = current_angle1
        #print(f"Moving servos to {current_angle} degrees")
    #    time.sleep(delay)

    

if __name__ == '__main__':
    init()
    main()
