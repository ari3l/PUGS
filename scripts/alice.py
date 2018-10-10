import random
from dh import generate_parameters
import hashlib


class Alice:

    def __init__(self):
        self.alpha = 0
        self.p = 0
        self.r = 0

    def setup(self, password, site):
        self.alpha, self.p = self.generate_alpha(password, site)
        self.r = random.randint(2, 2 ** 100)

    def calculate_h(self, pwd):
        # H(pwd|domain)
        rwd = int(hashlib.sha256(pwd).hexdigest(), 16)
        return rwd

    def generate_alpha(self, password, site):
        n = 100
        p, g = generate_parameters(n)
        h = self.calculate_h(str(password) + str(site))
        alpha = pow(g, h, p)
        return alpha, p

    def send_message(self):
        return pow(self.alpha, self.r, self.p), self.p

    def compute_b(self, b):
        return b ^ 1/self.r

    def __repr__(self):
        return str(self.__dict__)