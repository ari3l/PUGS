import random
from bob import Bob


class Alice:

    def __init__(self, alpha, p):
        self.alpha = alpha
        self.r = random.randint(2, 2 ** 100)
        self.p = p

    def send_message(self, p):
        a = pow(self.alpha, self.r, self.p)
        return a, p

    def receive_message(self, Bob):
        b = pow(a, self.k, self.p)

    def __repr__(self):
        return str(self.__dict__)