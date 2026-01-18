import socket


# Server's IP address and port to send to
UDP_IP = "127.0.0.1"
UDP_PORT = 42069
HELLO_MSG = b"HELLO"

BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

    sock.sendto(HELLO_MSG, (UDP_IP, UDP_PORT))

    # Optional: Receive a reply from the server
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Received reply from server: {data.decode('utf-8')}")

    while True:
        ...