import socket

HOST = "localhost"
PORT = 8001
PAYLOAD = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
BUFFER_SIZE = 4096

def main():
    try:
        # creates a new socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except OSError as e:
            print("There was an error creating the socket", e)
            return

        address = (HOST, PORT)
        s.connect(address)

        try:
            s.sendall(PAYLOAD.encode())
        except socket.error:
            print("There was an error sending the information")
            return

        s.shutdown(socket.SHUT_WR)

        all_data = b''
        # checks for responses that are greater than the BUFFER_SIZE
        while True:
            data = s.recv(BUFFER_SIZE)

            if not data:
                break

            all_data += data
        
        print(all_data)
    except Exception as e:
        print("There was an error", e)
    finally:
        s.close()

main()