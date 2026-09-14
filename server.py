import argparse
import socket
import struct
import sys
import threading


def recieve_data(conn: socket.socket):
    try:
        from_client = ""
        while True:
            sz: int = struct.unpack("<I", conn.recv(4))[0]
            data = conn.recv(sz)
            if not data:
                break
            from_client += data.decode()
            print(f"Recieved Data: {from_client}")
            break
    finally:
        conn.close()


def run_server(ip, port):
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((ip, port))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        threading.Thread(target=recieve_data, args=(conn,)).run()


def get_args():
    parser = argparse.ArgumentParser(description="Create server listener.")
    parser.add_argument("client_ip", type=str, help="the client's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    return parser.parse_args()


def main():
    """
    Implementation of CLI and reciving data to server.
    """
    args = get_args()
    try:
        run_server(args.client_ip, args.server_port)
        print("Done.")
    except Exception as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
