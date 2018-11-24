import socket
import pickle
from bob import Bob

HOST = '127.0.0.1'
PORT = 50007


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    conn, addr = s.accept()

    print 'RECEIVED CONNECTION ', addr

    while True:
        data = conn.recv(4096)
        if not data:
            break

        alice_data = pickle.loads(data)  # tuple containing alpha and p from alice

        alpha = alice_data[0]
        p = alice_data[1]

        bob = Bob()
        bob.setup(alpha, p)
        b = bob.receive_message()  # bob sends back b

        serialized_data = pickle.dumps(b)
        conn.sendall(serialized_data)
    s.close()


if __name__ == '__main__':
    main()