'''
Program to run the robot based on the output of A-star algorithm
Need to convert the output from type .csv to type .json
'''

from pybricks.hubs import EV3Brick
# from robot import *
from output2commands.robot import *
import json
import csv


ev3 = EV3Brick()
robot = Robot(l_motor_port=Port.A, r_motor_port=Port.B,
                l_ultra_port=Port.S1, r_ultra_port=Port.S2, 
                wheel_diameter=55.5, axle_track=104,
                tile_len = 230, # 23cm, longest side of the robot
                motor_direction=Direction.COUNTERCLOCKWISE)
#read file
json_file = open('output2commands/position.json', 'r')
json_data = json_file.read()

#parse
obj = json.loads(json_data)
pos_list = obj['data'] # list of positions

#Read each step and move robot
count = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
head = UP # place robot with its head up

for enum, i  in enumerate(pos_list):
    print(i)
    #get pos to go
    curPosX = i[0]
    curPosY = i[1]

    #moving robot by curPos and prevPos
    #Go staight 
    # if count != 0:  #stay still at first position
    robot.forward()
    
    #check next step to decide turn or not
    if count < len(pos_list) - 1:  #last position not check anymore
        nextPosX = pos_list[count+1][0]
        nextPosY = pos_list[count+1][1]
        if head == UP:
            if nextPosX == curPosX and curPosY > nextPosY: #turn left(head left)
                robot.turn_left()
                head = LEFT
            if nextPosX == curPosX and curPosY < nextPosY: #turn right(head right)
                robot.turn_right()
                head = RIGHT
            if nextPosX > curPosX and curPosY == nextPosY: #turn back(head down)
                robot.turn_back()
                head = DOWN
        elif head == DOWN:
            if nextPosX == curPosX and curPosY < nextPosY: #turn left(head left)
                robot.turn_right()
                head = LEFT
            if nextPosX == curPosX and curPosY > nextPosY: #turn right(head right)
                robot.turn_left()
                head = RIGHT
        elif head == LEFT:
            if nextPosY == curPosY and curPosX > nextPosX: #turn right(head up)
                robot.turn_right()
                head = UP
            if nextPosY == curPosY and curPosX < nextPosX: #turn left(head down)
                robot.turn_left()
                head = DOWN
        elif head == RIGHT:
            if nextPosY == curPosY and curPosX > nextPosX: #turn left(head up)
                robot.turn_left()
                head = UP
            if nextPosY == curPosY and curPosX < nextPosX: #turn right(head down)
                robot.turn_right()
                head = DOWN
    count+=1

