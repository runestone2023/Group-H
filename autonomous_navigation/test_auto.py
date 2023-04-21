# PROGRAM
# 1. robot keeps going ahead until it finds an blocking object
# 2. it checks the right. If there is nothing, it turns right and program goes back to 1
# 3. it checks the left. If there is nothing, it turns right and program goes back to 1
# 4. if both sides are blocked, it stops
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
rotate_motor = Motor(Port.C) # Head motor at port C

ultra_sensor = UltrasonicSensor(Port.S1) # Ultrasonic sensor at port 1

# Main program
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
ev3.speaker.say("start")

while True:
    robot.drive(200, 0) # driving forward at 200 millimeters per second
    while ultra_sensor.distance() > 150:
        wait(10) # literally doing nothing
    robot.stop()

    # Check right side
    rotate_motor.run_angle(200, 90) # turn head right
    wait(1000)
    print("Right:", ultra_sensor.distance())
    if ultra_sensor.distance() > 150:
        rotate_motor.run_angle(100, -90) # turn head straight
        robot.turn(90) # turn robot to the right
    else: # Check left side
        rotate_motor.run_angle(100, -180) # turn head left
        wait(1000)
        print("Left :", ultra_sensor.distance())
        if ultra_sensor.distance() > 150:
            rotate_motor.run_angle(100, 90) # turn head straight
            robot.turn(-90) # turn robot to the left
        else:
            rotate_motor.run_angle(100, 90) # turn head straight
            break

ev3.speaker.say("stop")