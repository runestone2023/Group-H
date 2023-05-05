import socketio
import socket

#robot_host = "192.168.2.2"
robot_host = "169.254.178.31"
robot_port = 5000  # socket server port number
robot_socket = socket.socket()  # instantiate
robot_socket.connect((robot_host, robot_port))  # connect to the server

sio = socketio.Client()

@sio.event
def connect():
    sio.emit('message', 'Robot')
    print("I'm connected!")

@sio.on('forward_robot')
def on_forward_robot(data):
    print(data)
    robot_socket.send("f".encode())  # send message
    data = robot_socket.recv(1024).decode()  # receive response

@sio.on('left_robot')
def on_stop_robot(data):
    print(data)
    robot_socket.send("l".encode())  # send message
    data = robot_socket.recv(1024).decode()  # receive response

@sio.on('right_robot')
def on_stop_robot(data):
    print(data)
    robot_socket.send("r".encode())  # send message
    data = robot_socket.recv(1024).decode()  # receive response

@sio.on('backwards_robot')
def on_stop_robot(data):
    print(data)
    robot_socket.send("b".encode())  # send message
    data = robot_socket.recv(1024).decode()  # receive response

@sio.on('stop_robot')
def on_stop_robot(data):
    print(data)
    robot_socket.send("s".encode())  # send message
    data = robot_socket.recv(1024).decode()  # receive response

@sio.on('serverMsg')
def on_serverMsg(data):
    print(data)

@sio.on('*')
def catch_all(event, data):   
    print("msg from webserver: '%s' " %data)


if __name__ == '__main__':
  sio.connect('http://localhost:3000')