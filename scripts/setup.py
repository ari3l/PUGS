from dh import generate_parameters
import random

ALICE_FILE = 'alice.txt'
BOB_FILE = 'bob.txt'

if __name__ == '__main__':
    p, g = generate_parameters(100)
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