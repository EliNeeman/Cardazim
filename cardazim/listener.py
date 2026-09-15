from connection import Connection
import socket
class Listener:
    def __init__(self,port,host,backlog=1000):
        self.port = port
        self.host = host
        self.backlog = backlog
        self.sock = None
    
    def __repr__(self):
        return f'Listener(host={self.host}, port="{self.port}", backlog={self.backlog})'
    
    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.backlog)
    
    def accept(self):
        conn, addr = self.sock.accept()
        return Connection(conn)
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self,*args):
        self.sock.close()