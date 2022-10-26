import socket
from Interactive import *

ADDR = "127.0.0.1"
PORT = 9999

if __name__ == "__main__":
    interactiveService = InteractiveService()

    s = socket.socket()
    print("Socket successfully created")

    s.bind((ADDR, PORT))
    print("socket bind to %s" %(PORT))

    s.listen(2)
    
    while True:    
        print("Wait for new connection.")
        conn, addr = s.accept()

        interactiveService.serve(conn)
        conn.close()