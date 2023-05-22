'''
Program to run the robot based on the output of A-star algorithm
Need to convert the output from type .csv to type .json
'''

# from robot import *
from output2commands.robot import *

# Create Robot instance
robot = Robot(l_motor_port=Port.B, r_motor_port=Port.A,
                l_ultra_port=Port.S2, r_ultra_port=Port.S3, 
                color_port=Port.S1, tile_len = 300, # 30cm - tile side length
                wheel_diameter=55.5, axle_track=104,
                motor_direction=Direction.CLOCKWISE)

# PROGRAM
# robot.run_path('position5.json')
robot.auto_single_path()


