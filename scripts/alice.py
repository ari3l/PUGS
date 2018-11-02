import random
import hashlib
import os
import string
from dh import modinv
import db
import re


class Alice:

    def __init__(self):
        self.alpha = 0
        self.p = 0
        self.r = 0
        self.g = 0

    def setup(self, password, site):

        if os.path.exists("alice.txt"):
            # read the number from the file
            file = open("alice.txt", "r")
            file_str = file.read()
            file_str = file_str.split(",")
            self.p = int(file_str[0])
            self.g = int(file_str[1])
        print('P value is: ' + str(self.p))
        print('G value is: ' + str(self.g))
        self.r = random.randint(2, (self.p - 1)/2)
        print('R value is: ' + str(self.r))
        self.alpha = self.generate_alpha(password, site)
        print('Alpha is: ' + str(self.alpha))

    def calculate_hash(self, password, site):
        # H(pwd|domain)
        string_concat = ''
        database = db.Database()
        database.create_db()
        timestamp = database.retrieve(site)
        database.store(site)
        string_concat = str(password) + str(site) + str(timestamp)
        h = int(hashlib.sha256(string_concat).hexdigest(), 16)
        return h

    def generate_alpha(self, password, site):
        h = self.calculate_hash(password, site)
        print('H value is: ' + str(h))
        alpha = pow(self.g, h, self.p)
        return alpha

    def send_message(self):
        return pow(self.alpha, self.r, self.p), self.p

    def compute_rwd(self, b, category):
        inverse = modinv(self.r, (self.p-1)/2)

        message = pow(b, inverse, self.p)
        print('\nb^ inverse of r (r^-1 mod p-1/2): {0}'.format(message))
        rwd_str = str(message)

        print('\nRWD: {0}'.format(rwd_str))

        super_simple_list = list(string.ascii_letters)
        simple_list = list(string.ascii_letters + string.digits)
        symbols_list = ['-', '_', '*', '%', '!', '@', '$', '#', '^', '&']
        complex_list = list(simple_list + symbols_list)

        if category == 'simple':
            new_rwd = self.map_algorithm(simple_list, rwd_str)
        elif category == 'super-simple':
            new_rwd = self.map_algorithm(super_simple_list, rwd_str)
        else:
            new_rwd = self.map_algorithm(complex_list, rwd_str)

        print('\nNew RWD: {0}'.format(new_rwd))

    def generate_more_characters(self, rwd_str):
        split_str_rwd = str(rwd_str.split())
        hashlist = []
        for piece in split_str_rwd:
            hashlist.append(hashlib.sha512(piece + rwd_str).hexdigest())
        return hashlist

    def map_algorithm(self, category_list, rwd_str):
        hashlist = self.generate_more_characters(rwd_str)
        hashlist_string = ''.join(hashlist)
        chaya_cant_function = re.findall('..', hashlist_string)
        new_rwd = ''
        count = 1

        for thing in chaya_cant_function:
            if count <= 16:
                x = int(thing, 16)/2

                if x in range(0, len(category_list)-1):
                    count += 1
                    new_rwd += category_list[x]

        return new_rwd

    def __repr__(self):
        return str(self.__dict__)
