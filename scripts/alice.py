import random
from dh import generate_parameters
import hashlib
import os
import string

class Alice:

    def __init__(self):
        self.alpha = 0
        self.p = 0
        self.r = 0
        self.g = 0

    def setup(self, password, site, n):

        if os.path.exists("alice.txt"):
            # read the number from the file
            file = open("alice.txt", "r")
            file_str = file.read()
            file_str = file_str.split(",")
            self.r = int(file_str[0]) #TODO r should NOT be saved
            self.p = int(file_str[1])
            self.g = int(file_str[2])
            print "Read r " + str(self.r) + " and p" + str(self.p) + "g: " + str(self.g)
        else:
            self.p, self.g = generate_parameters(n)
            self.r = random.randint(2, ((p - 1)/2))
            f = open("alice.txt", "w")
            f.write(str(self.r) + "," + str(self.p) + "," + str(self.g))
            f.close()
        self.alpha = self.generate_alpha(password, site)

    def calculate_hash(self, password, site):
        # H(pwd|domain)
        string_concat = str(password) + str(site)
        h = int(hashlib.sha256(string_concat).hexdigest(), 16)
        return h

    def generate_alpha(self, password, site):
        h = self.calculate_hash(password, site)
        alpha = pow(self.g, h, self.p)
        return alpha

    def send_message(self):
        return pow(self.alpha, self.r, self.p), self.p

    def compute_rwd(self, b, category):
        message = b ** (1 / self.r)
        print('\nValue received from Bob: {0}'.format(message))
        rwd_str = str(message)
        rwd = hashlib.sha256(rwd_str).hexdigest()
        print('\nRWD: {0}'.format(rwd))

        simple_list = list(string.ascii_letters + string.digits)
        symbols_list = ['-', '_', '*', '%', '!', '@', '$', '#', '^', '&']
        complex_list = list(simple_list + symbols_list)
        new_rwd = ''

        if category == 'simple':
            new_rwd = self.map_algorithm(simple_list, rwd)
        else:
            new_rwd = self.map_algorithm(complex_list, rwd)

        print('\nNew RWD: {0}'.format(new_rwd))

    def map_algorithm(self, category_list, rwd):
        new_rwd = '' #new rwd will be of length 16 (max length)
        n = 4
        split_rwd = [rwd[i:i+n] for i in range(0, len(rwd), n)]

        for x in split_rwd:
            index = int(x, 16) % len(category_list) - 1
            new_rwd += category_list[index]

        return new_rwd

    def __repr__(self):
        return str(self.__dict__)
