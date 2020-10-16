from Crypto.Cipher import AES
from flask import Flask
import string
from base64 import b64encode
import os
import struct

#cleartext = bytes(str(input("Ingrese el mensaje a cifrar: ")),'utf-8')
cleartext=b'holamundoholamundo'
#password = bytes(str(input("Ingrese la clave de 16 caracteres: ")),'utf-8')
password=b'clave secreta fuerte muy segura1'
cipher = AES.new(password , AES.MODE_CFB)
encrypted = cipher.encrypt(cleartext)
print(encrypted)
encrypted= b64encode(encrypted).decode('utf-8')
password= password.decode('utf-8')
iv = b64encode(cipher.iv).decode('utf-8')
print(encrypted)
print(password)
print(iv)
file = open("index.html","w")
file.write("<body>"+os.linesep)
file.write("<h1>¡Bienvenido Agente!</h1>\n<br>"+os.linesep)
file.write("<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/V4MF2s6MLxY\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe><br>"+os.linesep)
file.write("<form id =\""+password+"\"method=\"get\" action=\"/tepasas\">"+os.linesep)
file.write("<button id=\""+encrypted+"\" name =\""+iv+"\"type=\"submit\">El mensaje cifrado esta aquí</button>"+os.linesep)
file.write("</form>"+os.linesep)
file.write("</body>"+os.linesep)
file.close()

app = Flask(__name__)
@app.route("/")
def hello():
    return ("<body><h1>¡Bienvenido Agente!</h1><br><iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/V4MF2s6MLxY\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe><br><form id =\""+password+"\"method=\"get\" action=\"/tepasas\"><button id=\""+encrypted+"\" name =\""+iv+"\" type=\"submit\">El mensaje cifrado esta aquí</button></form></body>")

@app.route("/tepasas")
def hello2():
    return("<h1>¡Te pasaste!</h1><br><iframe ALIGN=center width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/-hEt6hUA3rQ\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe><br><form method=\"get\" action=\"/\"><button type=\"submit\">Una oportunidad más</form>")

if __name__ == "__main__":
    app.run()
