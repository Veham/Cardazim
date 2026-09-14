import socket
import struct


class Connection:
    def __init__(self, conn: socket.socket):
        self.conn = conn

    def __repr__(self) -> str:
        return f"<Connection from {self.conn.getsockname} to {self.conn.getpeername}>"

    def send_message(self, message: bytes):
        sz = len(message)
        sf = struct.Struct(f"<I{sz}s")
        self.conn.send(sf.pack(sz, message))

    def recieve_message(self) -> str:
        sz: int = struct.unpack("<I", self.conn.recv(4))[0]
        data = self.conn.recv(sz)
        return data.decode()

    @classmethod
    def connect(cls, host, port):
        conn = Connection(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        conn.conn.connect((host, port))
        return conn

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return self
