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

    def calculate_hash(self, password, site):
        # H(pwd|domain)
        h = str(password) + str(site)
        rwd = int(hashlib.sha256(h).hexdigest(), 16)
        return rwd

    def generate_alpha(self, password, site):
        n = 100
        p, g = generate_parameters(n)
        h = self.calculate_hash(password, site)
        alpha = pow(g, h, p)
        return alpha, p

    def send_message(self):
        return pow(self.alpha, self.r, self.p), self.p

    def compute_b(self, b):
        return b ^ (1/self.r)

    def __repr__(self):
        return str(self.__dict__)