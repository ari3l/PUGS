from scripts import clientExample
from scripts import setup
import random
import string


def main():
    failure_counter = 0
    success_counter = 0
    setup.setup(100)
    setup.main()
    for i in range(100000):
        print("COUNT:" + str(i))
        try:
            username = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            password = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            site = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)]) + '.com'
            category = random.choice(['simple', 'super-simple', 'complex'])

            clientExample.main(username, password, site, category)
            success_counter += 1
        except:
            failure_counter += 1
    print("Successes: " + str(success_counter))
    print("Failures: " + str(failure_counter))


if __name__ == '__main__':
    main()
