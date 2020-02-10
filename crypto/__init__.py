# Source, generic code that is used in the creation or breaking of ciphers
from .src.eea import eea # Extended Euclidean Algorithm
from .src.fast_power import fast_power
from .src.legendre_symbol import legendre_symbol
from .src.mod_inv import mod_inv # Modular Inverse
from .src.mod_sqrt import mod_sqrt # Modular Square Root

# Cryptanalysis Tools, code that is used ONLY to break ciphers
from .cryptanalysis.crt import crt # Chinese Remainder Theorem
from .cryptanalysis.naive_factor import naive_factor
from .cryptanalysis.order import order
from .cryptanalysis.bsgs import bsgs # (Baby Step Giant) Step Discrete Logarithm
from .cryptanalysis.small_primes_generator import small_primes_generator

# Ciphers
# Public Key Ciphers, the actual encryption and decryption, asymmetric key
from .ciphers.public.diffie_hellman import diffie_hellman
from .ciphers.public.el_gammal import el_gammal
# Private Key Ciphers the actual encryption and decryption, symmetric key
from .ciphers.private.shift import shift # Substitution Cipher

# Elliptic Curve Cryptography Utilities
# ECC Source
from .ecc.src.curve import curve

# ECC Cryptanalysis
from .ecc.cryptanalysis.ecc_dlog_brute import ecc_dlog_brute # Elliptic Curve Cryptography Discrete Logarithm Brute Force Algorithm
from .ecc.cryptanalysis.ecc_dlog_lsbs import ecc_dlog_lsbs # Elliptic Curve Cryptography Discrete Logarithm Little Step Big Step
from .ecc.cryptanalysis.lenstras_algorithm import lenstras_algorithm

#ECC Public Ciphers
from .ecc.ciphers.public.ecc_diffie_hellman import ecc_diffie_hellman # Elliptic Curve
from .ecc.ciphers.public.ecc_el_gammal import ecc_el_gammal # Elliptic Curve
