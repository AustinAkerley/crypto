import random
class ecc_diffie_hellman(object):

    def __init__(self, curve = None, P = None):
        self.curve = curve;
        self.P = P

    def private_keygen(self):
        self.private_key = random.randint(1, self.curve.modulus)
        return self.private_key;

    def public_keygen(self, curve = None, P = None, private_key = None):
        if curve is not None:
            self.curve = curve;
        if P is not None:
            self.P = P;
        if private_key is not None:
            self.private_key = private_key;

        if None in [self.curve, self.P, self.private_key]:
            return None;

        self.QA = self.curve.multiply(self.P, self.private_key);
        return self.QA

    def symmetric_keygen(self, QB = None, private_key = None ):
        if private_key is not None:
            self.private_key = private_key
        if None in [self.curve, self.private_key, QB]:
            return None;
        
        if isinstance(QB, int):
            y2 = QB ** 3 
        return self.curve.multiply(QB, self.private_key);
