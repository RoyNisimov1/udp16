import socket
import threading
import mss
import mss.tools

class Server:
    HOST = "0.0.0.0"
    PORT = 42069
    BUFFER_SIZE = 1024

    clients = set()

    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((Server.HOST, Server.PORT))
            t = threading.Thread(target=self.handle, args=[s])
            t.start()
            while True:
                data, client_address = s.recvfrom(Server.BUFFER_SIZE)

                if not data:
                    break

                decoded_data = data.decode('utf-8')
                print(f"Received data from {client_address}: {decoded_data}")

                self.clients.add(client_address)

    def handle(self, s: socket.socket):
        while True:
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                screenshot = sct.grab(monitor)
                data = mss.tools.to_png(screenshot.rgb, screenshot.size)

            for client in self.clients:
                s.sendto(data, client)


