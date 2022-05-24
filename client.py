# Import socket module
import socket            
 

s = socket.socket()        
port = 8080             
s.connect(('127.0.0.1', port))

while True:
    i = input(">")
    s.send(i.encode())
s.close()    