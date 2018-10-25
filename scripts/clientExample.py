
import argparse
from alice import Alice
from bob import Bob



def main():
    args = parse_args()
    username = args.username
    password = args.password
    site = args.site
    category = args.category

    alice = Alice()
    alice.setup(password, site)

    a, p = alice.send_message()
    print('\na value (or alpha^r mod p): {0}'.format(a))
    bob = Bob()
    bob.setup(a, p)

    b = bob.receive_message()
    print('\nb value (or a^k mod p): {0}'.format(b))
    print('\nalpha raised to k mod p: {0}'.format(pow(alice.alpha, bob.k, p)))
    alice.compute_rwd(b, category)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='username for site')
    parser.add_argument('--password', help='master password entry')
    parser.add_argument('--site', help='domain')
    parser.add_argument('--category', help= 'enter simple or complex based on whether or not there are symbols in the password')
   
    return parser.parse_args()


if __name__ == '__main__':
    main()
