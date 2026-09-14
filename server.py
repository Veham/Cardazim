import argparse
import socket
import struct
import sys
import threading
import listener
import connection


def recieve_data(conn: connection.Connection):
    print(f"Recieved Data: {conn.recieve_message()}")


def run_server(host, port):
    with listener.Listener(host, port) as my_listener:
        while True:
            with my_listener.accept() as conn:
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
