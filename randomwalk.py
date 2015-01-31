from sr.robot import *
import time
from random import randint

"""RANDOM WALK"""

R = Robot()

right = R.motors[0].m0
left = R.motors[0].m1

RIGHT_ADJUST = 1
LEFT_ADJUST = 1.17

POWER = 40

MAX_TURN_TIME = 1
MAX_DRIVE_TIME = 5

def drive(t, direction):
    if direction == 0:
        direction = -1
    right.power = POWER * RIGHT_ADJUST * direction
    left.power = POWER * LEFT_ADJUST * direction
    time.sleep(t)

def turn(t, direction):
    # 0 or -1 = left, 1 = right
    if direction == 0:
        direction = -1
    right.power = POWER * RIGHT_ADJUST * direction
    left.power = POWER * LEFT_ADJUST * -direction
    time.sleep(t)

def stop():
    right.power = 0
    left.power = 0

def randomMove():
    d = randint(0,1)
    turn_d = randint(0,1)

    t = randint(0,MAX_DRIVE_TIME*10)/10
    turn_t = randint(0,MAX_TURN_TIME*10)/10

    drive(t, d)
    turn(turn_d, turn_t)

for i in range(4):
    randomMove()
    
