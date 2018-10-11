import random
from dh import generate_parameters
import hashlib
import os


class Alice:

    def __init__(self):
        self.alpha = 0
        self.p = 0
        self.r = 0
        self.g = 0

    def setup(self, password, site):
        n = 100


        self.r = 43

        if os.path.exists("alice.txt"):
            # read the number from the file
            file = open("alice.txt", "r")
            file_str = file.read()
            file_str = file_str.split(",")
            self.r = int(file_str[0])
            self.p = int(file_str[1])
            self.g = int(file_str[2])
            print "Read r " + str(self.r) + " and p" + str(self.p) + "g: " + str(self.g)
        else:
            self.p, self.g = generate_parameters(n)
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

    def compute_b(self, b):
        return b ^ (1 / self.r)

    def __repr__(self):
        return str(self.__dict__)
