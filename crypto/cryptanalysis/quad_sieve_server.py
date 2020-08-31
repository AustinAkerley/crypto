#!/usr/bin/python3
# Title: Quadratic Sieve Server
# Creator: Austin Akerley
# Date Created: 08/02/2020
# Last Editor: Austin Akerley
# Date Last Edited: 08/02/2020
# Associated Book Page Nuber: 143

import math
import socket
import threading
import time
import json
import os
import random
import hashlib

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from crypto.src.fast_power import fast_power
from crypto.src.random_prime import random_prime
from crypto.src.eea import eea
from crypto.cryptanalysis.small_primes_generator import small_primes_generator
from crypto.ciphers.public.diffie_hellman import diffie_hellman

class quad_sieve_server:
    def __init__(self, N, host="127.0.0.1" , port = 8080, max_clients = 10):
        # Stuff for Factoring N
        self.N = N # Number we're trying to factor
        self.p = None # One of the factors
        sqrt_N = math.ceil(math.sqrt(N))
        client_start = sqrt_N

        # Key Exchange Stuff
        self.num_bits = 1024
        self.g = 627
        # 1024 bit prime
        self.prime = 141199525667038352636920821715116445202630978908141173487202253927127061789925035463047283768430777013812580603104122671560093443005183176870200142845014982808309967794530653687731235509456107113775212576133189854093007959960811860733386252666094296835126236318134884937455365078575914066091711109932325373697
        self.private_key = random.randint(1, self.prime-1)
        self.dh = diffie_hellman(self.g, self.private_key, self.prime)
        self.my_public_key = self.dh.gen_my_public_key()

        # Server & Socket Stuff
        self.max_clients = max_clients
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.settimeout(2)
        print("Server started")
        print("Waiting for client request..\n\n")
        threads = []

        self.bit_row_to_x = {}

        # Server Loop
        while self.p == None:
            newpid = os.fork()
            if newpid == 0:
                for thread in threads:
                    self.bit_row_to_x.update(thread.get_new_entries())
                    for bit_mat in self.bit_row_to_x:
                        print("LEN MATRIX: "+str(len(bit_mat)))
                print("NUM ENTRIES: "+str(len(self.bit_row_to_x)))
                with open('entries.json', 'w') as my_json:
                    json.dump(self.bit_row_to_x, my_json)
                os._exit(0)
            else:
                server.listen(max_clients)
                client = None
                try:
                     client, client_address = server.accept()
                except:
                    why = True
                if client is not None:
                    client_stop = client_start + 1000000
                    newthread = client_thread(client_address, client, N, client_start, client_stop, self.my_public_key, self.private_key, self.g, self.prime)
                    client_start = client_stop
                    newthread.start()
                    print("NEW THREAD! | SYM KEY: "+str(newthread.symmetric_key))
                    threads.append(newthread)




class client_thread(threading.Thread):
    def __init__(self,client_address, client, N, start_num, stop_num, public_key, private_key, g, prime):
        # Client Info
        threading.Thread.__init__(self)
        self.client = client
        self.client_address = client_address

        # Bit Mapping to y2 and x
        self.y_sqrd_to_x = {}
        self.bit_map_to_y2 = {}

        # Factorization Info
        self.N = N
        self.start_num = start_num
        self.stop_num = stop_num

        # AES Stuff
        self.g = g
        self.iv = 325014111296431816994499323111810629932
        self.iv = self.iv.to_bytes(16, "little")
        self.prime = prime
        self.my_public_key = public_key
        self.private_key = private_key
        self.client_public_key = None
        self.symmetric_key = None
        self.dh = diffie_hellman(self.g, self.private_key, self.prime)
        self.dh.set_public_key(self.my_public_key)
        self.dh.gen_symmetric_key()
        self.backend = default_backend()

        self.num_entries = 0
        self.bit_row_to_x = {}


    def run(self):
        print ("\nConnection from: \nADDRESS: " + str(self.client_address) + "\nSOCK: "+str(self.client)+"\n\n")

        # Get client public key
        self.client_public_key = self.recv("public_key : ")
        print("CLIENT PUB KEY : " + str(self.client_public_key))

        # Give client my key
        print("SERVER PUB KEY : "+str(self.my_public_key))
        self.send("public_key : ", self.my_public_key)

        # Compute symmetric key
        self.dh.gen_symmetric_key(self.client_public_key, self.private_key)
        self.symmetric_key = self.dh.symmetric_key
        self.symmetric_key = hashlib.sha256((self.symmetric_key).to_bytes(128, 'little')).digest()
        print("SYMMETRIC KEY : " + str(self.symmetric_key )+"\n\n")

        # Symmetric key created make the cipher
        self.cipher = Cipher(algorithms.AES(self.symmetric_key), modes.CBC(self.iv), backend=self.backend)
        self.encryptor = self.cipher.encryptor()
        self.decryptor = self.cipher.decryptor()

        time.sleep(0.5)

        # Send and Receive encrypted stuff now
        self.send("N : ", self.N)
        self.send("start : ", self.start_num)
        self.send("stop : ", self.stop_num)

        # Recieve entries to table
        self.end = False
        i = 0
        while not self.end:
            new_x = self.recv("x : ")
            new_row = self.recv("bit_matrix : ", ret_int=False)
            self.bit_row_to_x.update({new_row:new_x})
            self.num_entries += 1
            #print("Number of Entries: "+str(self.num_entries))



    def get_new_entries(self):
        copy_bit_row_to_x = self.bit_row_to_x
        self.bit_row_to_x = {}
        return copy_bit_row_to_x

    def send(self, key, value):
        resp = None
        data = bytes((key + str(value)), 'UTF-8')
        while resp != "resp":
            self.client.sendall(data)
            resp = self.client.recv(4096).decode()

    def recv(self, key, ret_int=True):
        value = None
        while value == None:
            data = self.client.recv(4096)
            potential_value = data.decode()
            if key in potential_value:
                print("POT VALUE: "+str(potential_value))
                num = potential_value.split(key, 1)[1]
                if num.isdigit() and ret_int:
                    value = int(num)
                else:
                    value = num
            elif "end" in potential_value:
                self.end = True
                print("END")
                break
        resp = bytes(("resp"), 'UTF-8')
        self.client.sendall(resp)
        return value

    def send_enc(self, key, value):
        data = bytes((key + str(value)), 'UTF-8')
        print(" LEN : " + str(len(data)))
        ct = self.encryptor.update(data) + self.encryptor.finalize()
        self.client.sendall(ct)

    def recv_enc(self, key):
        value = None
        while value == None:
            data = self.client.recv(4096)
            potential_value = (self.decryptor.update(ct) + self.decryptor.finalize()).decode()
            print(potential_value)
            if key in potential_value:
                num = potential_value.split(key, 1)[1]
                if num.isdigit():
                    value = int(num)
        return value


if __name__ == '__main__':
    N = 660419183488531 * 473534564775287
    print("N: "+str(N))
    print("N Bits: "+str(len(bin(N)[2:])))
    quad_sieve_server(N)
