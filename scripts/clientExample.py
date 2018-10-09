import hashlib
import argparse
#from alice import Alice
from dh import generate_parameters
import random
#from bob import Bob

#TODO: add retry ?


def calculate_rwd(pwd):
    #H(pwd|domain)
    rwd = int(hashlib.sha256(pwd).hexdigest(), 16)
    return rwd


def main():
    args = parse_args()
    username = args.username
    password = args.password
    site = args.site
    n = 100

    p, g = generate_parameters(n)

    h = calculate_rwd(str(password) + str(site))

    print('h value: {0}'.format(h))

    r = random.randint(2, 2 ** n)
    k = random.randint(2, 2 ** n)

    alpha = pow(g, h, p) #alpha is g^h mod p
    print('Alpha: {0}'.format(alpha))


    a = pow(alpha, r, p) #a is alpha^r mod p
    print('\nAlice sends to Bob: ' + str(a))

    b = pow(a, k, p) #bob has a^k mod p
    print('\nBob sends back to Alice: {0}'.format(b))

    computed_value = b ^ 1/r
    print('\nComputed value: {0}'.format(computed_value))

    hashed_message = str(computed_value)
    actually_hashed = hashlib.sha256(hashed_message).hexdigest()
    print('\nNew hash value: {0}'.format(actually_hashed))

    other_value = pow(r, -1) % (p-1)/2
    print('\nOther value: {0}'.format(other_value))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', default='username', help='username for site')
    parser.add_argument('--password', default='password', help='master password entry')
    parser.add_argument('--site', default='google.com', help='domain')
    return parser.parse_args()


if __name__ == '__main__':
    main()