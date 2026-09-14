import socket
import struct
class Connection:
    def __init__(self,sock:socket.socket):
        self.sock = sock
    
    def __repr__(self):
        local_address, local_port = self.sock.getsockname()
        remote_address, remote_port = self.sock.getpeername()
        return f'<Connection  from {local_address}:{local_port} to {remote_address}:{remote_port}>'

    @classmethod        
    def connect(cls,host,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return Connection(sock)
    
    def close(self):
        self.sock.close()
    
    def send_message(self, message: bytes):
        message_size = len(message)
        packed_message = struct.pack(f'<i{message_size}s',message_size, message)
        self.sock.sendall(packed_message)
    
    def receive_message(self):
        packed_data  = self.sock.recv(1024)
        data_size = struct.unpack('<i',packed_data[:4])[0]
        data = struct.unpack(f'<i{data_size}s',packed_data)[1].decode()
        return data

    def __enter__(self):
        return self
    
    def __exit__(self,*args):
        self.close()
    
