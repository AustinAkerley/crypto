# Source, generic code that is used in the creation or breaking of ciphers
from .src.eea import eea # Extended Euclidean Algorithm
from .src.mod_inv import mod_inv # Modular Inverse
from .src.fast_power import fast_power
from .src.decode_unicode import decode_unicode
from .src.encode_unicode import encode_unicode
from .src.crt import crt # Chinese Remainder Theorem
from .src.mod_sqrt import mod_sqrt # Modular Square Root
from .src.small_primes_generator import small_primes_generator
from .src.legendre_symbol import legendre_symbol
# Cryptanalysis Tools, code that is used ONLY to break ciphers
from .cryptanalysis.tonelli_shanks import tonelli_shanks
from .cryptanalysis.ecc_dlog_brute import ecc_dlog_brute # Elliptic Curve Cryptography Discrete Logarithm Brute Force Algorithm
from .cryptanalysis.ecc_dlog_lsbs import ecc_dlog_lsbs # Elliptic Curve Cryptography Discrete Logarithm Little Step Big Step
from .cryptanalysis.order import order
from .cryptanalysis.lenstras_algorithm import lenstras_algorithm
# Ciphers, the actual encryption and decryption
from .ciphers.substitution import substitution # Substitution Cipher
from .ciphers.diffie_hellman import diffie_hellman
from .ciphers.el_gammal import el_gammal
from .ciphers.ecc_diffie_hellman import ecc_diffie_hellman # Elliptic Curve
# Elliptic Curve Cryptography utilities
from .ecc.curve import curve
