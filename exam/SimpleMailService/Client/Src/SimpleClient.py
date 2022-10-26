import socket

ADDR = "127.0.0.1"
PORT = 9999

if __name__ == "__main__":
    s = socket.socket()
    s.connect((ADDR, PORT))
    while True:
        msg =  s.recv(1024).decode()
        
        if msg == "__QUIT":
            break

        print(msg)
        s.send(input().encode())


    s.close()