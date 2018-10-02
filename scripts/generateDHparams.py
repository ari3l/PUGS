from dh import generate_prime
import random


def generate_factors(prime_num):
    factors = []
    p = prime_num - 1
    for i in range(1, prime_num):
        if p % i == 0:
            factors.append(i)
    factors.remove(1)
    factors.remove(p)

    return factors


def generate_z(prime_number):
    z = []
    for i in range(1, prime_number):
        z.append(i)

    return z


def generate_cyclic_group(prime_number):
    prime_number_set = generate_z(prime_number)
    factors = generate_factors(prime_number)
    generator_list = []

    for number in prime_number_set:

        list = [number**x % prime_number for x in factors]

        if 1 not in list:
            generator_list.append(number)

    return generator_list


def main():

    prime_number = generate_prime(10) #range between 1 and 1024

    cyclic_group = generate_cyclic_group(prime_number)

    alpha = random.choice(cyclic_group)

    print "Prime Number Value: " + str(prime_number)
    print "Generator (alpha) Value: " + str(alpha)


if __name__ == '__main__':
    main()




