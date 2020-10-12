from flask import Flask
import hashlib
import math
import os
from Crypto.Cipher import AES
import string
from base64 import b64encode

vector = 16
llave = 32
LargoSalt = 16

cleartext = b'esto es una prueba'
cleartext2 = str(b64encode(cleartext).decode())
print(cleartext2)
password = b'password es una mala clave'
salt = os.urandom(LargoSalt)
#print(salt)
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=vector + llave)
iv = derived[0:vector]
key = derived[vector:]

encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext)
encrypted= str(b64encode(encrypted).decode())
key= str(b64encode(key).decode())
iv= str(b64encode(iv).decode())
#salt = encrypted[0:LargoSalt]
#derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=vector + llave)
#iv = derived[0:vector]
#key = derived[vector:]
#cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[LargoSalt:])

app = Flask(__name__)
@app.route("/")
def hello():
    return ("<body><h1>¡Bienvenido Agente!</h1><br><iframe ALIGN=center id=\""+iv+"\" width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/yXkV0h3eM20\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe><br><form method=\"get\" action=\"/tepasas\"><button id=\""+encrypted+"\" name=\""+key+"\"type=\"submit\">El mensaje cifrado esta aquí</form></body>")

@app.route("/tepasas")
def hello2():
    return("<h1>¡Te pasaste!</h1><br><iframe ALIGN=center width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/-hEt6hUA3rQ\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe><br><form method=\"get\" action=\"/\"><button type=\"submit\">Una oportunidad más</form>")

if __name__ == "__main__":
    app.run()
