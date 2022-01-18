import socket

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((HOST, PORT))
    s.listen(1)

    print("listening")

    while True:
        conn, address = s.accept()
        # should I ignore this?
        # fetch data sent to main server
        data_to_send = conn.recv(BUFFER_SIZE)

        # configure parameters for Google
        proxy_host = "www.google.com"
        proxy_port = 80
        buffer_size = 1024

        print("Connecting to Google")
        proxy_end = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_end.connect((proxy_host, proxy_port))
        # send data to proxy
        proxy_end.send(data_to_send)
        proxy_end.shutdown(socket.SHUT_WR)
        # get results 
        # response to proxy's result
        data = proxy_end.recv(buffer_size)         # TODO: create a while loop 

        proxy_end.close()

        conn.send(data)
        conn.close()


        # connect to Google.com

main()