import socket

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # to send input to the terminal
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind((HOST, PORT))

    # allows a backlog of 2 requests
    s.listen(2)
    print("listening")

    # Make socket to constantly listen to requests
    while True:
        conn, address = s.accept()
        print("Connected by ", address)

        data_received = conn.recv(BUFFER_SIZE)
        conn.send(data_received)
        print("DATA", data_received)
        conn.close()
    

main()