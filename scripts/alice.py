import hashlib
from bob import Bob


class Alice:

    def __init__(self, alpha, r, p):
        self.alpha = alpha
        self.r = r
        self.p = p

    def receive_message(self, Bob):

        return Bob
        # s = message ** 1/self.r
        # hex_string = hex(s).rstrip("L").lstrip("0x") or "0"
        # return int(hashlib.sha256(hex_string).hexdigest(),16)

    def __repr__(self):
        return str(self.__dict__)