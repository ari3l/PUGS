import random

class Bob:

    def __init__(self):
        self.k = 22
        self.a = 0
        self.p = 0

    def setup(self, a, p):
        self.a = a
        self.p = p

    def receive_message(self):
        return pow(self.a, self.k, self.p)

    def __repr__(self):
        return str(self.__dict__)