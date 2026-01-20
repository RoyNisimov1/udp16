import time
from socket import socket
from hashlib import sha256

class Protocol:


    @staticmethod
    def send_files(s: socket, client: str, data: bytes, chunk_size: int = 1024):
        hashed = sha256(data).hexdigest()
        s.sendto(hashed.encode(), client)
        for i in range(0, len(data), chunk_size):
            chunk = data[i: i + chunk_size]
            s.sendto(chunk, client)
        s.sendto(b"EOF", client)

    @staticmethod
    def recv_files(s: socket, chunk_size: int = 1024, verbose=False) -> bytes:
        hashed, address = s.recvfrom(64)
        data = b""
        while True:
            packet, address = s.recvfrom(chunk_size)
            if packet == b"EOF":
                break
            data+=packet
        if (h:=sha256(data).hexdigest().encode()) != hashed and verbose:
            print("Hashes don't match")
            print(f"{hashed}")
            print(f"{h}")
        return data



