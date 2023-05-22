from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import json

class Robot(DriveBase):
    '''Wrapper class for class DriveBase'''
    def __init__(self, l_motor_port, r_motor_port, 
                    l_ultra_port, r_ultra_port,
                    color_port, tile_len,
                    wheel_diameter, axle_track, 
                    motor_direction=Direction.CLOCKWISE):
        '''
        Args:
        l_motor_port - Port that left motor is plugged e.g. Port.A
        r_motor_port - Port that right motor is plugged e.g. Port.D
        l_ultra_port - Port that left ultrasonic sensor is plugged e.g. Port.S1
        r_ultra_port - Port that right ultrasonic sensor is plugged e.g. Port.S1
        color_port - Port that color sensor is plugged
        wheel_diameter - diameter of motor wheels
        axle_track - distance between two motor wheels
        motor_direction - Direction of motor, default value is 'clockwise'
        tile_len - Length of a side of the tile, 
                    which is equal to the length of the longest side of the self
        '''
        self.l_motor = Motor(l_motor_port, positive_direction=motor_direction)
        self.r_motor = Motor(r_motor_port, positive_direction=motor_direction)
        super().__init__(self.l_motor, self.r_motor, wheel_diameter, axle_track)
        self.l_ultra = UltrasonicSensor(l_ultra_port)
        self.r_ultra = UltrasonicSensor(r_ultra_port)
        self.color = ColorSensor(color_port)
        self.ev3 = EV3Brick()
        self.tile_len = tile_len

    def ultra_vals(self):
        ''' Get left and right ultra sensors' value '''
        l = self.l_ultra.distance()
        r = self.r_ultra.distance()
        print("Left:", l, " Right:", r)
        return l, r

    def color_val(self):
        ''' Get value of color sensor '''
        color = self.color.color()
        print('Color: ', color)
        return color

    def forward(self):
        print("Go forward")
        self.straight(self.tile_len) 

    def turn_right(self):
        print("Turn right")
        self.turn(90)

    def turn_left(self):
        print("Turn left")
        self.turn(-90)

    def turn_back(self):
        print("Turn back")
        self.turn(180)

    def forward_stable(self):
        ''' 
        Robot keeps going stably between two walls until it reaches an intersection 
        '''
        print("Forward stable")
        cnt = 0
        flag = False
        while True:
            l, r = self.ultra_vals()
            wait(100)
            if l > 300 or r > 300:
                break

            elif flag or (l > 50 and r > 50): # good distance to 2 walls
                print('Good distance')
                cnt += 1
                if cnt == 2:
                    print('Good distance 2 times. Keep forward')
                    flag = True

            elif r < 50: # too close to right wall
                print('Veer left')
                self.turn(-20)
                self.straight(70)
                self.turn(20)

            elif l < 50: # too close to left wall
                print('Veer right')
                self.turn(20)
                self.straight(70)
                self.turn(-20)

            self.straight(100)

        return l, r

    def check_options(self):
        '''
        At the intersection, robot checks which direction it can go
        After this, A-star decides which way to go
        '''
        l, r = self.ultra_vals()
        left, right, forward = False, False, False
        if l > 300:
            print("Left:", l, "OK")
            left = True
            # More here
        if r > 300:
            print("Right:", r, "OK")
            right = True
            # More here

        self.turn(-90)
        r = self.r_ultra.distance()
        self.turn(+90)
        
        if r > 300:
            print("Forward:", r, "OK")
            forward = True
            # More here
        return left, right, forward

    def auto_single_path(self):
        ''' The robot finds its way to the end of a single path '''
        self.ev3.speaker.beep()
        while True:
            left, right, forward = self.check_options()
            color = self.color_val()
            print('Options (left, right, forward):', left, right, forward)
            # Currently, the robot goes only if one of the directions is availabe
            if not left and not right and forward:
                pass
            elif left and not right and not forward:
                self.turn_left()
            elif not left and right and not forward:
                self.turn_right()
            elif not left and not right and not forward and color != Color.GREEN:
                self.turn_back()
            else:
                self.turn_back()
                break
            self.forward()
        
        self.ev3.speaker.beep()
        print('END')

    def run_path(self, position_file):
        '''
        Args:
        position_file - path to .json file that store the path (output of A-star)
        '''
        # Read positions from .json file
        json_file = open(position_file, 'r')
        json_data = json_file.read()
        obj = json.loads(json_data)
        positions = obj['data'] # list of positions
        print('List of positions:', positions)

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
                    self.turn_left()
                    head = LEFT
                elif next_x == x and next_y > y: # turn right, head points right
                    self.turn_right()
                    head = RIGHT
                elif next_x > x and y == next_y: # turn back, head points downward
                    self.turn_back()
                    head = DOWN
                else: # case next_x < x and y == next_y: just go forward
                    pass

            elif head == DOWN:
                if next_x == x and next_y < y: # turn right, head points left
                    self.turn_right()
                    head = LEFT
                elif next_x == x and next_y > y: # turn left, head points right
                    self.turn_left()
                    head = RIGHT
                elif next_x < x and next_y == y: # turn back, head points up
                    self.turn_back()
                    head = UP
                else:
                    pass

            elif head == LEFT:
                if next_x == x and next_y > y: # turn back, head points right
                    self.turn_back()
                    head = RIGHT
                elif next_x < x and next_y == y: # turn right, head points up
                    self.turn_right()
                    head = UP
                elif next_x > x and next_y == y: # turn left, head points down
                    self.turn_left()
                    head = DOWN
                else:
                    pass

            elif head == RIGHT:
                if next_x == x and next_y < y: # turn back, head points left
                    self.turn_back()
                    head = LEFT
                elif next_x < x and next_y == y: # turn left, head points up
                    self.turn_left()
                    head = UP
                elif next_x > x and next_y == y: # turn right, head points down
                    self.turn_right()
                    head = DOWN
                else:
                    pass
            
            self.ev3.speaker.beep()
            self.forward()
            cnt += 1

        self.ev3.speaker.beep()
