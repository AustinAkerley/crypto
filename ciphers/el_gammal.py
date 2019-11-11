from src.fast_power import fast_power
import random
class el_gammal:

    def __init__(generator=None, modulus=None, private_key=None, public_key=None, cipher_text_1=None, cipher_text_2=None):
        if generator is not None:
            self.set_generator(generator)
        if modulus is not None:
            self.set_modulus(modulus)
        if private_key is not None:
            self.set_private_key(private_key)
        if public_key is not None:
            self.set_public_key(public_key)
        if cipher_text_1 is not None:
            self.set_cipher_text_1(cipher_text_1)
        if cipher_text_2 is not None:
            self.set_cipher_text_2(cipher_text_2)

    def set_generator(self, generator):
        self.generator=generator

    def set_modulus(self, modulus):
        self.modulus = modulus

    def set_private_key(self, private_key):
        self.private_key = private_key

    def set_public_key(self, public_key):
        self.public_key = public_key

    def set_cipher_text_1(self, cipher_text_1):
        self.cipher_text_1 = cipher_text_1

    def set_cipher_text_2(self, cipher_text_2):
        self.cipher_text_1 = cipher_text_1

    def gen_public_key(private_key=None, generator=None, modulus=None):
        if private_key is not None:
            self.set_private_key(private_key)
        if generator is not None:
            self.set_generator(generator)
        if modulus is not None:
            self.set_modulus(modulus)
        if None in [self.private_key, self.modulus, self.generator]:
            return None
        else:
            self.public_key = fast_power(self.generator, self.private_key, self.modulus)
            return self.public_key

    def encrypt(message=None, generator=None, public_key=None, modulus=None, k=None):
        if generator is not None:
            self.set_generator(generator)
        if public_key is not None:
            self.set_public_key(public_key)
        if modulus is not None:
            self.set_modulus(modulus)
        #Validate k
        if k is None:
            if self.modulus is not None:
                k = random.randint(2,self.modulus-2)
            else:
                return None
        elif k <= 1 or k>=self.modulus-1:
            print("Invalid k value")
            return None

        if isinstance(message, int):
            #Validate message
            if message <= 2 or message >= p-1:
                print("Invalid message size, must be in range 2-p-2")
                return None
            else:
                if None in [self.generator, self.public_key]
                self.cipher_text_1 = fast_power(self.generator)

        else:
            return None
