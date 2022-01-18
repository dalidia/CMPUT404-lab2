import socket

HOST = "localhost"
PORT = 8001
PAYLOAD = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
BUFFER_SIZE = 4096

def main():
    try:
        s = socket.socket(socket.AF_INET)
        s.connect((HOST, PORT))
        s.send(PAYLOAD.encode())
        # TODO: keeps checking for data
        s.shutdown(socket.SHUT_WR)
        x = s.recv(BUFFER_SIZE)
        print("x", x)
        # TODO: change exception
    except Exception as e:
        print("There was an error", e)
    finally:
        s.close()

main()