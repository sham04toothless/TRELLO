from djitellopy import tello
import Keypressmodule as kp
from time import sleep
import numpy as np
#####PARAMETERS####
fspeed = 117/10  # Forward Speed in cm/s
speed = 360/10 # Angular Speed in Degrees/s
interval = 0.25
##################
dinterval = fspeed*interval
ainterval = aspeed*interval



kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def getKeyboardInput():
    lr,fb,ud,yv = 0,0,0,0
    speed = 50

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey('RIGHT'):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey('DOWN'):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey('s'):
        ud = -speed

    if kp.getKey("a"):
        yv = speed
    elif kp.getKey('d'):
        yv = -speed

    if kp.getKey("q"):
        drone.land()
    if kp.getKey("e"):
        drone.takeoff()

    return [lr,fb,ud,yv]
while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = np.zeros((1000,1000,3),np.uint8)
