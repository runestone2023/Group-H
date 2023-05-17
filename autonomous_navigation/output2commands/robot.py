from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Robot(DriveBase):
    '''Wrapper class for class DriveBase'''
    def __init__(self, l_motor_port, r_motor_port, 
                    l_ultra_port, r_ultra_port,
                    wheel_diameter, axle_track, 
                    tile_len,
                    motor_direction=Direction.CLOCKWISE):
        '''
        Args:
        l_motor_port - Port that left motor is plugged e.g. Port.A
        r_motor_port - Port that right motor is plugged e.g. Port.D
        l_ultra_port - Port that left ultrasonic sensor is plugged e.g. Port.S1
        r_ultra_port - Port that right ultrasonic sensor is plugged e.g. Port.S1
        wheel_diameter - diameter of motor wheels
        axle_track - distance between two motor wheels
        motor_direction - Direction of motor, default value is 'clockwise'
        tile_len - Length of a side of the tile, 
                    which is equal to the length of the longest side of the robot
        '''
        self.l_motor = Motor(l_motor_port, positive_direction=motor_direction)
        self.r_motor = Motor(r_motor_port, positive_direction=motor_direction)
        super().__init__(self.l_motor, self.r_motor, wheel_diameter, axle_track)
        self.l_ultra = UltrasonicSensor(l_ultra_port)
        self.r_ultra = UltrasonicSensor(r_ultra_port)
        self.tile_len = tile_len

    def ultra_vals(self):
        ''' Get left and right ultra sensors' value '''
        l = self.l_ultra.distance()
        r = self.r_ultra.distance()
        print("Left:", l, " Right:", r)
        return l, r

    def forward(self):
        print("Going forward")
        self.straight(self.tile_len) 

    def backward(self):
        print("Going backward")
        self.straight(-1 * self.tile_len) 

    def turn_right(self):
        print("Turning right")
        self.turn(90)

    def turn_left(self):
        print("Turning left")
        self.turn(-90)

    def turn_back(self):
        print("Turning back")
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

    def auto(self):
        while True:
            left, right, forward = self.check_options()
            print('Options (left, right, forward):', left, right, forward)
            # Currently, the robot goes only if one of the directions is availabe
            if not left and not right and forward:
                self.forward_stable()
            elif left and not right and not forward:
                self.straight(130) 
                self.turn_left()
                self.straight(300) # go to the next tile after turning left
                self.forward_stable()
            elif not left and right and not forward:
                self.straight(130)
                self.turn_right()
                self.straight(300) # go to next tile
                self.forward_stable()
            else:
                print('END')
                break  

        

