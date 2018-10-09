import random

class Bob:

    def __init__(self, a, p):
        self.a = a
        self.k = random.randint(2, 2 ** 100)
        self.p = p

    def receive_message(self, a, p):

    def __repr__(self):
        return str(self.__dict__)