
import argparse
from alice import Alice
from bob import Bob


def main(username, password, site, category, update):

    alice = Alice()
    alice.setup(username, password, site, update)

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
    parser.add_argument('--username', help='username for site', required=True)
    parser.add_argument('--password', help='master password entry', required=True)
    parser.add_argument('--site', help='domain', required=True)
    parser.add_argument('--update', help= 'update password', required=False)
    parser.add_argument('--category', help= 'enter simple or complex based on whether or not there are symbols in the password', required=True)
    #parser.add_argument('--change-pwd', help='enter yes if you want to change the password. enter no otherwise', required=True) no longer using this as it is based on 30 days
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    username = args.username
    password = args.password
    site = args.site
    category = args.category
    update = args.update
    main(username, password, site, category, update)
