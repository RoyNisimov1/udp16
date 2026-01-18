from socket import socket


class Protocol:


    @staticmethod
    def send_files(s: socket, client: str, data: bytes, chunk_size: int = 1024):
        sequence_number = 0
        while len(data) != 0:
            seqdata = data[:chunk_size]
            data = data[chunk_size:]

            header = f"{sequence_number}|{len(seqdata)}|".encode('utf-8')

            packet = header + seqdata






