import argparse
import sys

###########################################################
####################### YOUR CODE #########################
###########################################################
from listener import Listener
from connection import Connection
import socket
import struct
import threading


def run_server(server_ip, server_port):
    """
    Run a server in address (server_ip, server_port)
    """
    while True:
        with Listener(server_port, server_ip) as listener:
            with listener.accept() as connection:
                t = threading.Thread(target=handle_connection, args=(connection,))
                t.start()


def handle_connection(connection, logger=print):
    message = connection.receive_message()
    logger(f"Recived data: {message}")


###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description="Start a server.")
    parser.add_argument("server_ip", type=str, help="the server's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    return parser.parse_args()


def main():
    """
    Implementation of CLI and setting up a server.
    """
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
        print("Done.")
    except Exception as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
