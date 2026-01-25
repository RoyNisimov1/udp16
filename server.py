import socket
import threading
import mss
import mss.tools
import io
from PIL import Image

from protocol import Protocol


class Server:
    HOST = "0.0.0.0"
    PORT = 42069
    BUFFER_SIZE = 1024

    clients = set()

    def __init__(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.bind((Server.HOST, Server.PORT))
                t = threading.Thread(target=self.handle, args=[s])
                t.start()
                while True:
                    try:
                        data, client_address = s.recvfrom(Server.BUFFER_SIZE)

                        if not data:
                            break

                        decoded_data = data.decode('utf-8')
                        print(f"Received data from {client_address}: {decoded_data}")

                        self.clients.add(client_address)
                    except Exception:
                        ...
        except Exception:
            ...



    def handle(self, s: socket.socket):

        while True:
            try:
                with mss.mss() as sct:
                    monitor = sct.monitors[1]
                    img = sct.grab(monitor)
                    pil_img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
                    byte_io = io.BytesIO()
                    pil_img.save(byte_io, format="JPEG", quality=85)
                    jpeg_bytes = byte_io.getvalue()

                for client in self.clients:
                    Protocol.send_files(s, client, jpeg_bytes)
            except Exception:
                ...


if __name__ == "__main__":
    Server()