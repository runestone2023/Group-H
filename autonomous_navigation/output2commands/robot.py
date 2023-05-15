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
        

        

