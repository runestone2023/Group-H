import rpyc

print(rpyc.__version__)

# Create a RPyC connection to the remote ev3dev device.
# Use the hostname or IP address of the ev3dev device.
# If this fails, verify your IP connectivty via ``ping X.X.X.X``
conn = rpyc.classic.connect("192.168.2.2")

# import ev3dev2 on the remote ev3dev device
ev3dev2_speaker = conn.modules['ev3dev2.sound']

spkr = ev3dev2_speaker.Sound()

spkr.speak('Hello, I am Robot')