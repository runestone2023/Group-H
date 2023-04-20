#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Configure the robot
ev3 = EV3Brick()
right_motor = Motor(Port.D) # Right motor at port D
left_motor = Motor(Port.A) # Left motor at port A
ultra_sensor = UltrasonicSensor(Port.S1) # Ultrasonic sensor at port 1

# Main program
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
ev3.speaker.beep() # beeps to signal START

# The robot will turn around if it detects an object
while True:
    robot.drive(200, 0) # driving forward at 200 millimeters per second
    while ultra_sensor.distance() > 300:
        wait(10) # literally doing nothing
    # Drive backward for 300 millimeters.
    robot.straight(-300)

    # Turn around by 360 degrees
    robot.turn(360)
    break

ev3.speaker.beep() # beeps to signal STOP
