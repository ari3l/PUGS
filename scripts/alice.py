import random
import hashlib
import os
import string
from dh import modinv
import db
import re
import math
import json

class Alice:

    def __init__(self):
        self.alpha = 0
        self.p = 0
        self.r = 0
        self.g = 0

    def setup(self, username, password, site, update):

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
        self.alpha = self.generate_alpha(username, password, site, update)
        print('Alpha is: ' + str(self.alpha))

    def calculate_hash(self, username, password, site, update):
        # H(pwd|domain)
        string_concat = ''
        database = db.Database()
        if update == 'yes':
            database.update(site)
            timestamp = database.retrieve(site)
        else:
            timestamp = database.retrieve(site)
            database.store(site)
        json_arr = [username, password, site, timestamp]
        json_array_str = json.dumps(json_arr) #str(username) + str(password) + str(site) + str(timestamp)
        h = int(hashlib.sha256(json_array_str).hexdigest(), 16)
        return h

    def generate_alpha(self, username, password, site, update):
        h = self.calculate_hash(username, password, site, update)
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
        hashlist = []
        pwd_length = 16
        for i in range(pwd_length):
            hashlist.append(hashlib.sha512(str(i) + rwd_str).hexdigest())
        return hashlist

    def map_algorithm(self, category_list, rwd_str):
        hash_list = self.generate_more_characters(rwd_str)
        rwd_list = []

        for h in hash_list:
            character = re.findall('..', h)
            for c in character:
                divisor = 2**math.floor(math.log(float(256)/len(category_list), 2)) #CASTING TO A FLOAT BECAUSE PYTHON 2.7 IS HORRIBLE
                x = int(c, 16)/divisor

                if x in range(0, len(category_list)-1):
                    rwd_list.append(category_list[int(x)])
                    break

        return ''.join(rwd_list)

    def __repr__(self):
        return str(self.__dict__)
