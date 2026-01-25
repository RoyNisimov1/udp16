import socket
import pygame
import io
from protocol import Protocol

class Client:
    UDP_IP = "127.0.0.1"
    UDP_PORT = 42069
    HELLO_MSG = b"HELLO"

    BUFFER_SIZE = 1024
    def __init__(self):
        self.running = True
        clock = pygame.time.Clock()
        try:

            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

                sock.sendto(Client.HELLO_MSG, (Client.UDP_IP, Client.UDP_PORT))

                screen = pygame.display.set_mode((1000,600))


                while self.running:
                    try:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.running = False
                                break
                        try:
                            screenshot = Protocol.recv_files(sock, Client.BUFFER_SIZE)
                            image_stream = io.BytesIO(screenshot)
                            img = pygame.image.load(image_stream, ".jpeg").convert_alpha()
                            screen.blit(img, (0, 0))
                        except:
                            ...
                        pygame.display.flip()
                        clock.tick(30)
                    except Exception:
                        ...
        except Exception as e:
            print(e)

if __name__ == "__main__":
    pygame.init()
    Client()