import socket


s = socket.socket()
port = 8080
s.bind(('192.168.1.36', port))
print("socket binded to %s" % (port))

s.listen(5)

while True:

    print("waiting for client..")
    conn, addr = s.accept()
    print("client connected: ",conn)
    
    with conn:
        while True:
            data = conn.recv(2)
            print("recieved:", data)
            if not data:
                print("disconnected")
                break
    
    
    # c.close()

    
