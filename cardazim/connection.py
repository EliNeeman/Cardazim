import socket
import struct


class Connection:
    def __init__(self, sock: socket.socket):
        self.sock = sock

    def __repr__(self):
        local_address, local_port = self.sock.getsockname()
        remote_address, remote_port = self.sock.getpeername()
        return f"<Connection  from {local_address}:{local_port} to {remote_address}:{remote_port}>"

    @classmethod
    def connect(cls, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return Connection(sock)

    def close(self):
        self.sock.close()

    def send_message(self, message: bytes):
        message_size = len(message)
        packed_message = struct.pack(f"<i{message_size}s", message_size, message)
        self.sock.sendall(packed_message)

    def receive_message(self):
        message_size = struct.unpack("<i", self.sock.recv(4))[0]
        message = self.sock.recv(message_size)
        data = struct.unpack(f"<{message_size}s", message)[0].decode()
        return data

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
