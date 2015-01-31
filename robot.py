from sr import *
import time

R = Robot()

front_right_motor = R.motors[0].m0
front_left_motor  = R.motors[1].m1
rear_motor        = R.motors[0].m1

FRONT_LEFT_FACTOR  = 1.17
FRONT_RIGHT_FACTOR = 1

def drive(speed):
    front_right_motor.power = -speed * FRONT_RIGHT_FACTOR
    front_left_motor.power  = -speed * FRONT_LEFT_FACTOR

def stop():
    front_right_motor.power = 0
    front_left_motor.power = 0
    rear_motor = 0

def move(umbrellas):
    drive(40 if umbrellas > 0 else -40)
    time.sleep(2 * abs(umbrellas))
    stop()

move(2)
move(-0.5)
