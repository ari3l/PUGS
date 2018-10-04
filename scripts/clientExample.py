import hashlib
import argparse
from alice import Alice
from dh import generate_parameters
import random
from bob import Bob


def calculate_rwd(pwd):
    #H(pwd|domain)
    rwd = int(hashlib.sha256(pwd).hexdigest(), 16)
    return rwd


def main():
    args = parse_args()
    username = args.username
    password = args.password
    site = args.site
    n = 10
    p, g = generate_parameters(n)

    print('P: {0} G: {1}'.format(p, g))

    rwd = 7

    print('Randomly generated password: {0}'.format(rwd))

    r = random.randint(2, 2 ** n)
    k = random.randint(2, 2 ** n)

    alpha = pow(g, rwd, p)
    print('Alpha: {0}'.format(alpha))

    alice = Alice(alpha, r, p)
    a = pow(alice.alpha, r, p)
    print('\nAlice\'s keys are: G: {0} P: {1} R: {2}'.format(alice.alpha, alice.p, alice.r))
    print('\nAlice sends to Bob: ' + str(a))

    bob = Bob(alice.alpha, k, alice.p)
    b = bob.get_message()

    print('\nBob\'s keys are: G: {0} P: {1} K: {2}'.format(bob.g, bob.p, bob.k))
    print('\nBob sends back to Alice: {0}'.format(b))

    received_message = alice.receive_message(bob)
    print(received_message)
    if pow(a, received_message.k, p) == pow(bob.get_message(), alice.r, p):
        print('\nAlice and Bob both computed: {0}'.format(pow(a, received_message.k, p)))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='username for site')
    parser.add_argument('--password', help='master password entry')
    parser.add_argument('--site', help='domain')
    return parser.parse_args()


if __name__ == '__main__':
    main()