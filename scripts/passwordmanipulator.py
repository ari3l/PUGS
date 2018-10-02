import argparse
import hashlib


def calculate_rwd(pwd):
    #H(pwd|domain)
    rwd = hashlib.sha256(pwd).hexdigest()

    return rwd


def main():
    args = parse_args()
    username = args.username
    password = args.password
    site = args.site

    rwd = calculate_rwd(password + site)
    print('Randomly generated password: {0}'.format(rwd))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='username for site')
    parser.add_argument('--password', help='master password entry')
    parser.add_argument('--site', help='domain')
    return parser.parse_args()


if __name__ == '__main__':
    main()