class substitution:
    #Class variables
    _MODE = ["alphabetic", "ascii", "ascii_ext", "unicode"]
    mode = "ascii"
    mod = 128
    cipher_text = []
    plain_text = []
    key = 0

    def __init__(self, key = None, plain_text = None, cipher_text = None, mode=None):
        if mode is not None:
            self.set_mode(mode)
        else:
            self.set_mode(self._MODE[1])
            print("Invalid mode type [%s] setting it to ascii" % mode)
        if cipher_text is not None:
            self.set_cipher_text(cipher_text) # List of strings
        if plain_text is not None:
            self.set_plain_text(plain_text) # List of strings
        if key is not None:
            self.set_key(key) #Integer

    def set_mode(self, mode):
        if mode in self._MODE:
            self.mode = mode
            if self.mode == self._MODE[0]:
                self.mod = 26
            elif self.mode == self._MODE[1]:
                self.mod = 128
            elif self.mode == self._MODE[2]:
                self.mod = 256
            elif self.mode == self._MODE[3]:
                self.mod = 0x110000
        else:
            self.mode = None
            self.mod = None

    def set_plain_text(self, plain_text):
        self.plain_text = []
        if isinstance(plain_text, str):
            if self.validate(plain_text):
                self.plain_text = [plain_text]
            else:
                self.plain_text = []
        elif isinstance(plain_text, list):
            for text in plain_text:
                if self.validate(text):
                    self.plain_text.append(text)
                else:
                    self.plain_text.append("")
        elif isinstance(plain_text, dict):
            for key in plain_text:
                text = plain_text[key]
                if self.validate(text):
                    self.plain_text.append(text)
                else:
                    self.plain_text.append("")
        else:
            try:
                text = str(plain_text)
                if self.validate(text):
                    self.plain_text = [text]
                else:
                    self.plain_text.append("")
            except:
                print("Invalid input type [%s]" % type(plain_text))
                self.plain_text = []

    def set_cipher_text(self, cipher_text):
        self.cipher_text = []
        if isinstance(cipher_text, str):
            if self.validate(cipher_text):
                self.cipher_text = [cipher_text]
            else:
                self.cipher_text = []
        elif isinstance(cipher_text, list):
            for text in cipher_text:
                if self.validate(text):
                    self.cipher_text.append(text)
                else:
                    self.cipher_text.append("")
        elif isinstance(cipher_text, dict):
            for key in cipher_text:
                text = cipher_text[key]
                if self.validate(text):
                    self.cipher_text.append(text)
                else:
                    self.cipher_text.append("")
        else:
            try:
                text = str(cipher_text)
                if self.validate(cipher_text):
                    self.cipher_text = [cipher_text]
                else:
                    self.cipher_text.append("")
            except:
                print("Invalid input type [%s]" % type(plain_text))
                self.cipher_text = []

    def set_key(self, key):
        if isinstance(key, int):
            self.key = key % self.mod
        elif isinstance(key, str):
            if key.isdigit():
                self.key = int(key) % self.mod
            elif len(key) == 1:
                if self.mode == self._MODE[0]:
                    if ord(key)<97:
                        self.key = ord(key)-65 # convert char to key
                    if ord(key)<128:
                        self.key = ord(key)-97 # convert char to key
                    else:
                        self.key = None
                else:
                    self.key = ord(key)
            else:
                self.key = 0
                print("Invalid input value [%s] and type [%s]" % key, type(key))
        else:
            print("Invalid input type %s" % type(key))

    def validate(self, text):
        if self.mode == self._MODE[0]:
            if not isinstance(text, str):
                print("Invalid type [%s]" % type(text))
                return False
            for char in text:
                if not (65<=ord(char)<=90 or 97<=ord(char)<=122 or ord(char)==32):
                    print("Invalid char [%s] for [%s] mode" % (char, self.mode))
                    return False
        elif self.mode == self._MODE[1]:
            if not isinstance(text, str):
                print("Invalid type [%s]" % type(text))
                return False
            for char in text:
                if ord(char)>128:
                    print("Invalid char [%s] for [%s] mode" % (char, self.mode))
                    return False
        elif self.mode == self._MODE[2]:
            if not isinstance(text, str):
                print("Invalid type [%s]" % type(text))
                return False
            for char in text:
                if ord(char)>256:
                    print("Invalid char [%s] for [%s] mode" % (char, self.mode))
                    return False
        elif self.mode == self._MODE[3]: #Impossible to hit
            if not isinstance(text, str):
                print("Invalid type [%s]" % type(text))
                return False
            for char in text:
                if ord(char)>0x110000:
                    print("Invalid char [%s] for [%s] mode" % (char, self.mode))
                    return False
        else:
            print("Invalid mode")
            return False
        return True

    def encrypt(self, add = True):
        self.cipher_text = [] # reset cipher_text
        for plain_string in self.plain_text:
            cipher_string = ""
            if plain_string == "" or plain_string ==None:
                cipher_string = ""
            else:
                for char in plain_string:
                    if self.mode == self._MODE[0]:
                        ascii_char = ord(char)
                        if ascii_char == 32:
                            cipher_string += char
                        elif ascii_char < 97:
                            if add:
                                cipher_string += chr(((ord(char)+self.key-65) % self.mod)+65)
                            else:
                                cipher_string += chr(((ord(char)-self.key-65) % self.mod)+65)
                        elif ascii_char < 128:
                            if add:
                                cipher_string += chr(((ord(char)+self.key-97) % self.mod)+97)
                            else:
                                cipher_string += chr(((ord(char)-self.key-97) % self.mod)+97)
                        else:
                            print("ascii_char range error")
                    else:
                        if add:
                            cipher_string += chr((ord(char)+self.key)%self.mod)
                        else:
                            cipher_string += chr((ord(char)-self.key)%self.mod)
            self.cipher_text.append(cipher_string)
        return self.cipher_text

    def decrypt(self, sub = True):
        self.plain_text = [] # reset cipher_text
        for cipher_string in self.cipher_text:
            plain_string = ""
            if cipher_string == "" or cipher_string ==None:
                plain_string = ""
            else:
                for char in cipher_string:
                    if self.mode == self._MODE[0]:
                        ascii_char = ord(char)
                        if ascii_char == 32:
                            plain_string += char
                        elif ascii_char < 97:
                            if sub:
                                plain_string += chr(((ord(char)-self.key-65) % self.mod)+65)
                            else:
                                plain_string += chr(((ord(char)+self.key-65) % self.mod)+65)
                        elif ascii_char < 128:
                            if sub:
                                plain_string += chr(((ord(char)-self.key-97) % self.mod)+97)
                            else:
                                plain_string += chr(((ord(char)+self.key-97) % self.mod)+97)
                        else:
                            print("ascii_char range error")
                    else:
                        if sub:
                            plain_string += chr((ord(char)-self.key)%self.mod)
                        else:
                            plain_string += chr((ord(char)+self.key)%self.mod)
            self.plain_text.append(plain_string)
        return self.plain_text
