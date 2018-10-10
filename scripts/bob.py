import random

class Bob:

    def __init__(self):
        self.k = random.randint(2, 2 ** 100)

    def setup(self, a, p):
        self.a = a
        self.p = p

    def receive_message(self, a, p):
        return pow(self.a, self.r, self.p)

    def compute_value(self, a):
        return pow(a, self.k, self.p)

    def __repr__(self):
        return str(self.__dict__)