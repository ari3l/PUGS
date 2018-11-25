import socket
import pickle
from alice import Alice
import ssl


def main():

    host_addr = '127.0.0.1'
    host_port = 8082
    server_sni_hostname = 'example.com'
    server_cert = 'server.crt'
    client_cert = 'client.crt'
    client_key = 'client.key'

    username = "ariel"
    password = "sfjdskljwljk"
    site = "apple.com"
    update = False
    category = 'complex'

    alice = Alice()
    alice.setup(username, password, site, update)
    a, p = alice.send_message()

    alice_tuple = (a, p)

    serialized_data = pickle.dumps(alice_tuple)

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)
    context.load_cert_chain(certfile=client_cert, keyfile=client_key)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = context.wrap_socket(s, server_side=False, server_hostname=server_sni_hostname)
    conn.connect((host_addr, host_port))
    print("SSL established. Peer: {}".format(conn.getpeercert()))
    conn.sendall(serialized_data)

    # get b from server (bob)
    bob_data = conn.recv(4096)
    b = pickle.loads(bob_data)

    conn.close()

    alice.compute_rwd(b, category)


if __name__ == '__main__':
    main()
