import socket
import pickle
from alice import Alice

HOST = '127.0.0.1'
PORT = 50007


def main():

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

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(serialized_data)
    data = s.recv(4096)
    s.close()

    # get b from bob
    b = pickle.loads(data)

    # Compute rwd
    alice.compute_rwd(b, category)


if __name__ == '__main__':
    main()
