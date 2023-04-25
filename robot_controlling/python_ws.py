import socketio
from clientROBOT import fwd, listen

# standard Python
sio = socketio.Client()

@sio.event
def connect():
    sio.emit('message', 'Robot')
    print("I'm connected!")

@sio.on('forward_robot')
def on_forward_robot(data):
    print(data)
    fwd()
    msg = listen()
    print("msg from robot '%s'" %format(msg[0]))


@sio.on('serverMsg')
def on_serverMsg(data):
    print(data)

@sio.on('*')
def catch_all(event, data):   
    print("msg from webserver: '%s' " %data)


if __name__ == '__main__':
  sio.connect('http://localhost:3000')
