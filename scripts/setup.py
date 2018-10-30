from dh import generate_parameters
import random
import argparse

ALICE_FILE = 'alice.txt'
BOB_FILE = 'bob.txt'


def setup(n):
    p, g = generate_parameters(n) #make command line argument
    k = random.randint(2, ((p - 1)/2))

    # Alice stuff
    alice_str = str(p) + ',' + str(g)

    # Bob stuff
    bob_str = str(p) + ',' + str(k)

    f = open(ALICE_FILE, "w")
    f.write(alice_str)
    f.close()

    f = open(BOB_FILE, "w")
    f.write(bob_str)
    f.close()


def main():
    args = parse_args()
    n = args.n_value
    setup(int(n))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n-value', default=100, help='n value for generating p and g parameters')

    return parser.parse_args()


if __name__ == '__main__':
    main()

