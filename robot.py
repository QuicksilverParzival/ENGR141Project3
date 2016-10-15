import nxt
import nxtConnect # has to be in search path

brickName = "Team38"
useUSB = False

brick = nxtConnect.btConnect(brickName)

from time import sleep
from nxt.motor import SynchronizedMotors


# see files in library ( /usr/local/lib/python2.7/dist-packages/nxt )
# for a more comprehensive list of ports / commands available 
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4


try:
    motorLeft = Motor(brick, PORT_A) # plug motor into Port A
    motorRight = Motor(brick, PORT_B) # plug motor into Port B
    motorBoth = nxt.SynchronizedMotors(motorRight, motorLeft, 0)
    ultraSensor = Ultrasonic(brick, PORT_1) # plug ultrasonic sensor into Port 1

    #motorSync = SynchronizedMotors(motorA, motorB, 10000)
    #motorSync.idle()
    while ultraSensor.get_sample() > 10:
        print("Current ultrasonic sensor state: {}".format(
            ultraSensor.get_sample()))
        motorBoth.run(power = -120)
        '''motorA.run(power = -128) #go forward
        motorB.run(power = -128) #go forward'''

finally:
    Motor(brick, PORT_A).idle() # otherwise motor keeps running
    Motor(brick, PORT_B).idle() # otherwise motor keeps running
    print("Terminating Program")
    brick.sock.close()
