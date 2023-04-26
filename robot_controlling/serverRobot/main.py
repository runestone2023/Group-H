#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

right_motor = Motor(Port.D) # Right motor at port D
left_motor = Motor(Port.A) # Left motor at port A
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)



# Write your program here.
# ev3.speaker.beep()

import socket

host = '0.0.0.0'
port = 5000  # initiate port no above 1024

server_socket = socket.socket()  # get instance

server_socket.bind((host, port))  # bind host address and port together

server_socket.listen(2)
conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))

while True:
    bytesToSend = str.encode("OK")
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    if data == "f":
      print("move forward")
      robot.drive(200, 0)
    elif data == "l":
      print("move left!")
      left_motor.run(200)
    elif  data == "r":
      right_motor.run(200)
    elif data == "b":
      print("move backwards")
      robot.drive(-200, 0)
    elif data == "s":
      robot.stop()
      print("stop!")
    elif data == "bye":
      break
    else:
      print("unrecognized message %s" % data)
      bytesToSend = str.encode("bad")
    conn.send(bytesToSend)  # send data to the client

conn.send(str.encode("goodbye"))  # send data to the client
conn.close()  # close the connection