import socket

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 5000)
bufferSize          = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def fwd():
  UDPClientSocket.sendto(str.encode("fwd"), serverAddressPort)

# def fwd():
#   UDPClientSocket.sendto(str.encode("fwd"), serverAddressPort)

# def fwd():
#   UDPClientSocket.sendto(str.encode("fwd"), serverAddressPort)

# def fwd():
#   UDPClientSocket.sendto(str.encode("fwd"), serverAddressPort)

def listen():
  msg = UDPClientSocket.recvfrom(bufferSize)
  return msg

