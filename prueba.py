import hashlib
import math
import os
import codecs
from Crypto.Cipher import AES

llave = 32
cleartext = b'holamundoholamundo'
password = b'clavesecreta1234'#16 caracteres
encrypted = AES.new(password , AES.MODE_CFB).encrypt(cleartext)
