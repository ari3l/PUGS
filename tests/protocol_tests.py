import random
import dh

def main():

    count = 30

    while count > 0:
        p, g = dh.generate_parameters(100)
        h = 613 # :)
        k = random.randint(2, (p - 1)/2)
        r = random.randint(2, (p - 1)/2)

        alpha = pow(g, h, p)
        a = pow(alpha, r, p)
        b = pow(a, k, p)

        inv = dh.modinv(r, (p-1)/2)
        calculate_thing1 = pow(b, inv, p)
        calculate_thing2 = pow(alpha, k, p)

        if calculate_thing1 == calculate_thing2:
            print "%d == %d" % (calculate_thing1, calculate_thing2)
        else:
            print "ERROR %d != %d" % (calculate_thing1, calculate_thing2)
            break

        count = count - 1;

if __name__ == '__main__':
    main()