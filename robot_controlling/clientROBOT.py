import socket

def start_client():
  host = "192.168.2.2"  # as both code is running on same pc
  port = 5000  # socket server port number
  client_socket = socket.socket()  # instantiate
  client_socket.connect((host, port))  # connect to the server

  client_socket.send("bye".encode())  # send message
  data = client_socket.recv(1024).decode()  # receive response
  return data # show in terminal

if __name__ == '__main__':
  print("Manual control")
  print("Give a commmand\nforward - f, left - l, right - r, back - b, stop - s")

  start_client()


