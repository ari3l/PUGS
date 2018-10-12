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
    category = args.category

    alice = Alice()
    alice.setup(password, site, 100)

    a, p = alice.send_message()

    bob = Bob()
    bob.setup(a, p)

    b = bob.receive_message()
    print('\nBob sends back to Alice: {0}'.format(b))

    alice.compute_rwd(b, category)
    # other_value = pow(r, -1) % (p-1)/2
    # print('\nOther value: {0}'.format(other_value))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='username for site')
    parser.add_argument('--password', help='master password entry')
    parser.add_argument('--site', help='domain')
    parser.add_argument('--category', help= 'enter simple or complex based on whether or not there are symbols in the password')
   
    return parser.parse_args()


if __name__ == '__main__':
    main()