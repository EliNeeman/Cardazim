import argparse
import sys

###########################################################
####################### YOUR CODE #########################
###########################################################
import socket
import struct
import threading
def run_server(server_ip, server_port):
    '''
    Run a server in address (server_ip, server_port)
    '''
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((server_ip, server_port))
            s.listen(1)
            conn, addr = s.accept()
            t = threading.Thread(target=handle_connection,args=(conn,))
            t.start()
            t.join()

def handle_connection(conn):
    with conn:
        packed_data  = conn.recv(1024)
        data_size = struct.unpack('<i',packed_data[:4])[0]
        data = struct.unpack(f'<i{data_size}s',packed_data)[1].decode()
        print(f'Recived data: {data}')

            


###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description='Start a server.')
    parser.add_argument('server_ip', type=str,
                        help="the server's ip")
    parser.add_argument('server_port', type=int,
                        help="the server's port")
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and setting up a server.
    '''
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
