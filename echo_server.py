import socket
import time

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024

def main():
    # creates a new socket
    try:
        s = socket.socket(socket.AF_INET)
        print("Socket was created")
    except OSError as e:
        print("There was an error creating the socket", e)
        return

    # to send input to the terminal
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    # bind socket to address
    address = (HOST, PORT)
    s.bind(address)

    # allows a backlog of 2 connections
    s.listen(2)
    print("Socket is listening...")

    # Make socket to constantly listen to connections
    while True:
        conn, address = s.accept()
        print("Connected by ", address)

        data_received = conn.recv(BUFFER_SIZE)
        time.sleep(0.5)
        conn.sendall(data_received)
        conn.close()


main()