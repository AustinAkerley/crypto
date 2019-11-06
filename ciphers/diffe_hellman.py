import fast_power
class diffe_hellman: #The major return value of this class is the symmetric_key which can be used in AES and DES
    generator = None
    private_key = None
    modulus = None
    public_key = None
    symmetric_key = None
    def __init__(generator=None, private_key=None, modulus=None, public_key=None, symmetric_key=None):
        self.set_generator(generator)
        self.set_private_key(private_key)
        self.set_modulus(modulus)
        self.set_public_key(public_key)
        self.set_symmetric_key(symmetric_key)

    def set_generator(generator):
        self.generator = generator

    def set_private_key(private_key):
        self.private_key = private_key

    def set_modulus(modulus):
        self.modulus = modulus

    def set_public_key(public_key):
        self.public_key = public_key

    def set_symmetric_key(symmetric_key):
        self.symmetric_key = symmetric_key

    def public_key():
        if (self.generator or self.private_key or self.modulus) is None:
            return None
        else:
            self.public_key = fast_power.fast_power(self.generator, self.private_key, self.modulus)
            return self.public_key

    def
