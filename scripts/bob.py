import os

BOB_FILE = 'bob.txt'


class Bob:

    def __init__(self):
        self.k = 0
        self.a = 0
        self.p = 0

    def setup(self, a, p):
        if os.path.exists(BOB_FILE):
            file = open(BOB_FILE, "r")
            file_str = file.read().split(',')
            self.p = int(file_str[0])
            self.k = int(file_str[1])
        self.a = a

    def receive_message(self):
        return pow(self.a, self.k, self.p)

    def __repr__(self):
        return str(self.__dict__)