'''
Program to run the robot based on the output of A-star algorithm
Need to convert the output from type .csv to type .json
'''

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick

import json
# from robot import *
from output2commands.robot import *

ev3 = EV3Brick()
ev3.speaker.beep()

# Read positions from .json file
json_file = open('position5.json', 'r')
json_data = json_file.read()
obj = json.loads(json_data)
positions = obj['data'] # list of positions
print('List of positions:', positions)

# Create Robot instance
robot = Robot(l_motor_port=Port.B, r_motor_port=Port.A,
                l_ultra_port=Port.S2, r_ultra_port=Port.S3, 
                wheel_diameter=55.5, axle_track=104,
                tile_len = 300, # 30cm - tile side length
                motor_direction=Direction.CLOCKWISE)

# Some notations
cnt = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
head = UP # place robot with its head up

for pos in positions:
    print('Cur: ', pos)
    x, y = pos

    if cnt >= len(positions) - 1: 
        break

    next_x = positions[cnt + 1][0]
    next_y = positions[cnt + 1][1]

    if head == UP:
        if next_x == x and next_y < y: # turn left, head points left
            robot.turn_left()
            head = LEFT
        elif next_x == x and next_y > y: # turn right, head points right
            robot.turn_right()
            head = RIGHT
        elif next_x > x and y == next_y: # turn back, head points downward
            robot.turn_back()
            head = DOWN
        else: # case next_x < x and y == next_y: just go forward
            pass

    elif head == DOWN:
        if next_x == x and next_y < y: # turn right, head points left
            robot.turn_right()
            head = LEFT
        elif next_x == x and next_y > y: # turn left, head points right
            robot.turn_left()
            head = RIGHT
        elif next_x < x and next_y == y: # turn back, head points up
            robot.turn_back()
            head = UP
        else:
            pass

    elif head == LEFT:
        if next_x == x and next_y > y: # turn back, head points right
            robot.turn_back()
            head = RIGHT
        elif next_x < x and next_y == y: # turn right, head points up
            robot.turn_right()
            head = UP
        elif next_x > x and next_y == y: # turn left, head points down
            robot.turn_left()
            head = DOWN
        else:
            pass

    elif head == RIGHT:
        if next_x == x and next_y < y: # turn back, head points left
            robot.turn_back()
            head = LEFT
        elif next_x < x and next_y == y: # turn left, head points up
            robot.turn_left()
            head = UP
        elif next_x > x and next_y == y: # turn right, head points down
            robot.turn_right()
            head = DOWN
        else:
            pass
    
    ev3.speaker.beep()
    robot.forward()
    cnt += 1

ev3.speaker.beep()
