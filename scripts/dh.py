#!/usr/bin/python
import random

_mrpt_num_trials = 60  # number of bases to test


def is_probable_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    False
    """
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert (2 ** s * d == n - 1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True  # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True  # no base tested showed n as composite


def generate_prime(n):
    p = 0

    while True:
        p = random.randint(0, 2 ** n)
        if is_probable_prime(p) and is_probable_prime((p - 1) / 2):
            break

    return p


def generate_parameters(n):

    p = 0

    while True:
        p = random.randint(0, 2**n)
        if is_probable_prime(p) and is_probable_prime((p-1)/2):
            break

    g = random.randint(0, 2**n)**2 % p
    return (p, g)


def main():
    n = 100
    parameters = generate_parameters(n)

    p, g = parameters

    x = random.randint(2, 2 ** n)
    y = random.randint(2, 2 ** n)

    print('p = ' + str(p))
    print('g = ' + str(g))
    print('x = ' + str(x))
    print('y = ' + str(y))

    alice = pow(g, x, p)

    print('\nAlice sends to Bob: ' + str(alice))

    bob = pow(g, y, p)

    print('Bob sends to Alice: ' + str(bob))

    if pow(alice, y, p) == pow(bob, x, p):
        print('\nAlice and Bob both computed ' + str(pow(alice, y, p)))


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


if __name__ == '__main__':
    main()
