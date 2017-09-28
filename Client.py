#Client Version
import socket

HOST = '10.0.20.50'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
msg = input("What do you want to send?")
msg = msg.encode('utf-8')
s.sendall(msg)

data = s.recv(1024)
print("Recieved Server")