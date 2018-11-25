import socket
import pickle
from bob import Bob
import ssl


def main():
    listen_addr = '127.0.0.1'
    listen_port = 8082
    server_cert = 'server.crt'
    server_key = 'server.key'
    client_certs = 'client.crt'

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_cert_chain(certfile=server_cert, keyfile=server_key)
    context.load_verify_locations(cafile=client_certs)

    bindsocket = socket.socket()
    bindsocket.bind((listen_addr, listen_port))
    bindsocket.listen(5)

    while True:
        print("Waiting for client")
        newsocket, fromaddr = bindsocket.accept()
        print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
        conn = context.wrap_socket(newsocket, server_side=True)
        print("SSL established. Peer: {}".format(conn.getpeercert()))

        data = conn.recv(4096)
        alice_data = pickle.loads(data)  # tuple containing alpha and p from alice
        alpha = alice_data[0]
        p = alice_data[1]

        bob = Bob()
        bob.setup(alpha, p)
        b = bob.receive_message()  # bob sends back b

        serialized_data = pickle.dumps(b)
        conn.sendall(serialized_data)

        conn.shutdown(socket.SHUT_RDWR)
        conn.close()


if __name__ == '__main__':
    main()
