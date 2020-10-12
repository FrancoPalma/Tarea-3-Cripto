import hashlib
import math
import os
import codecs
from Crypto.Cipher import AES

vector = 16
llave = 32
LargoSalt = 16

cleartext = b'prueba'
password = b'password es una mala clave'
salt = os.urandom(LargoSalt)
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=vector + llave)
iv = derived[0:vector]
key = derived[vector:]

encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext)
print(encrypted)

salt = encrypted[0:LargoSalt]
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=vector + llave)
iv = derived[0:vector]
key = derived[vector:]
cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[LargoSalt:])
print(cleartext)
