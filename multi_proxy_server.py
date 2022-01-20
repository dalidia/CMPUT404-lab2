import socket
from multiprocessing import Process

HOST = ''
PORT = 8001
BUFFER_SIZE = 1024

def main():
    # creates a new socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket was created")
    except OSError as e:
        print("There was an error creating the socket", e)
        return

    # to send input to the terminal
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind socket to address
    address = (HOST, PORT)
    s.bind(address)

    s.listen(1)
    print("Socket is listening...")

    # Make socket to constantly listen to connections
    while True:
        print("HERE")
        conn, address = s.accept()
        print("another")
        # fetch data sent to main server
        data_to_send = conn.recv(BUFFER_SIZE)

        # configure parameters to connect to Google
        final_host = "www.google.com"
        final_port = 80
        final_buffer_size = 1024

        print("Connecting to Google")
        # creates a new socket for the proxy
        try:
            proxy_end = socket.socket(socket.AF_INET)
            print("Proxy socket was created")
        except OSError as e:
            print("There was an error creating the socket", e)
            return

        final_address = (final_host, final_port)
        proxy_end.connect(final_address)

        process = Process(target=handle_connections, args=(conn, proxy_end, data_to_send, final_host, final_buffer_size))
        # to execute process in the background
        process.daemon = True
        process.start()

def handle_connections(conn, proxy_end, data_to_send, final_host, final_buffer_size):
    # proxy sends data
    print(f"Send respective data to {final_host}")
    proxy_end.sendall(data_to_send)

    proxy_end.shutdown(socket.SHUT_WR)

    # check for incoming data greater than the buffer size
    all_data = b''
    while True:
        data = proxy_end.recv(final_buffer_size)
        if not data:
            break
        all_data += data

    proxy_end.close()

    conn.sendall(all_data)
    conn.close()

main()