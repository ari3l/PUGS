class Bob:

    def __init__(self, g, k, p):
        self.g = g
        self.k = k
        self.p = p

    def get_message(self):
        return pow(self.g, self.k, self.p)

    def __repr__(self):
        return str(self.__dict__)