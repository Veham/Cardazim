import socket
import threading

import connection


class Listener:
    def __init__(self, host, port, backlog=1000):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __repr__(self) -> str:
        return f'Listener(port={self.port}, host="{self.host}", backlog = {self.backlog})'

    def start(self):
        self.serv.bind((self.host, self.port))
        self.serv.listen(self.backlog)

    def stop(self):
        self.serv.close()

    def accept(self):
        conn, _addr = self.serv.accept()
        return connection.Connection(conn)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.stop()
        return self
