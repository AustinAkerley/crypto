from crypto.src.fast_power import fast_power
from crypto.src.mod_inv import mod_inv
import random
class el_gammal:

    def __init__(self,generator=None, private_key=None, modulus=None, public_key=None, cipher_text_1=None, cipher_text_2=None):
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
        self.cipher_text_2 = cipher_text_2

    def gen_public_key(self, private_key=None, generator=None, modulus=None):
        if private_key is not None:
            self.set_private_key(private_key)
        if generator is not None:
            self.set_generator(generator)
        if modulus is not None:
            self.set_modulus(modulus)
        if None in [self.private_key, self.modulus, self.generator]:
            return None
        else:
            self.public_key = fast_power(self.generator, self.private_key, self.modulus)[0]
            return self.public_key

    def encrypt(self, message=None, generator=None, public_key=None, modulus=None, k=None):
        if generator is not None:
            self.set_generator(generator)
        if public_key is not None:
            self.set_public_key(public_key)
        if modulus is not None:
            self.set_modulus(modulus)
        #Validate k
        if k is None:
            if self.modulus is not None:
                self.k = random.randint(2,self.modulus-2)
                #print("k: "+str(self.k))
            else:
                return None
        elif k <= 1 or k>=self.modulus-1:
            print("Invalid k value")
            return None
        else:
            self.k = k
        if isinstance(message, int):
            #Validate message
            if message <= 2 or message >= self.modulus-1:
                print("Invalid message size, must be in range 2-p-2")
                return None
            else:
                if None not in [self.generator, self.public_key]:
                    self.message = message
                    self.cipher_text_1 = fast_power(self.generator, self.k, self.modulus)[0]
                    self.cipher_text_2 = (self.message*fast_power(self.public_key, self.k, self.modulus)[0]) % self.modulus
                    return [self.cipher_text_1, self.cipher_text_2]
                else:
                    print("Generator or public key is none")
                    return None
        else:
            return None

    def decrypt(self, generator=None, modulus=None, private_key=None, cipher_text_1=None, cipher_text_2=None):
        if private_key is not None:
            self.set_private_key(private_key)
        if generator is not None:
            self.set_generator(generator)
        if modulus is not None:
            self.set_modulus(modulus)
        if cipher_text_1 is not None:
            self.set_cipher_text_1(cipher_text_1)
        if cipher_text_2 is not None:
            self.set_cipher_text_2(cipher_text_2)

        if None not in [self.private_key, self.generator, self.modulus, self.cipher_text_1, self.cipher_text_2]:
            x = mod_inv(fast_power(self.cipher_text_1, self.private_key, self.modulus)[0], self.modulus)
            self.message = (x*self.cipher_text_2)%self.modulus
            return self.message
        else:
            return None
