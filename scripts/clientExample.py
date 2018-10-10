import hashlib
import argparse
from alice import Alice
from bob import Bob

#TODO: add retry ?


def main():
    args = parse_args()
    username = args.username
    password = args.password
    site = args.site

    alice = Alice()
    alice.setup(password, site)

    a, p = alice.send_message()
    print('\nAlice sends to Bob: ' + str(a))

    bob = Bob()
    bob.setup(a, p)

    b = bob.compute_value(a)
    print('\nBob sends back to Alice: {0}'.format(b))

    computed_value = alice.compute_b(b)
    print('\nComputed value: {0}'.format(computed_value))

    hashed_message = str(computed_value)
    actually_hashed = hashlib.sha256(hashed_message).hexdigest()
    print('\nNew hash value: {0}'.format(actually_hashed))

    # other_value = pow(r, -1) % (p-1)/2
    # print('\nOther value: {0}'.format(other_value))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', default='username', help='username for site')
    parser.add_argument('--password', default='password', help='master password entry')
    parser.add_argument('--site', default='google.com', help='domain')
    return parser.parse_args()


if __name__ == '__main__':
    main()