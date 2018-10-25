from scripts.dh import generate_prime
import random


def test_inverse(r, p, inv_r):
    t = inv_r % ((p - 1) / 2)
    assert t * r % ((p - 1) / 2) == 1


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


def main():
    p = generate_prime(100)
    print("Prime Number: " + str(p))
    r = random.randint(2, ((p - 1)/2))
    print("Random Number: " + str(r))
    inverse_r = modinv(r, ((p - 1) / 2))
    print("Inverse Number: " + str(inverse_r))
    test_inverse(r, p, inverse_r)


if __name__ == '__main__':
    main()
