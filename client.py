import socket

HOST = "www.google.com"
PORT = 80
PAYLOAD = f'GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n'
BUFFER_SIZE = 4096

def main():
    # creates a new socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket was created")
    except OSError as e:
        print("There was an error creating the socket", e)
        return

    # connect the socket
    address = (HOST, PORT)
    s.connect(address)
    print(f"Socket connect to {HOST}")

    try:
        s.sendall(PAYLOAD.encode())
    except socket.error:
        print("There was an error sending the information")
        return
    
    s.shutdown(socket.SHUT_WR)

    all_data = b''
    # check for incoming data greater than the buffer size
    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            break
        all_data += data

    print(all_data)    
    s.close()

main()