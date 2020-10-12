from Crypto.Cipher import AES
from flask import Flask
import string
from base64 import b64encode

cleartext = b'holamundoholamundo'
password = b'clavesecreta1234'#16 caracteres
encrypted = AES.new(password , AES.MODE_CFB).encrypt(cleartext)
encrypted= encrypted.decode('windows-1252')
password= password.decode('utf-8')
print(encrypted)
print(password)

app = Flask(__name__)
@app.route("/")
def hello():
    return ("<body><h1>¡Bienvenido Agente!</h1><br><iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/V4MF2s6MLxY\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe><br><form id =\""+password+"\"method=\"get\" action=\"/tepasas\"><button id=\""+encrypted+"\" type=\"submit\">El mensaje cifrado esta aquí</form></body>")

@app.route("/tepasas")
def hello2():
    return("<h1>¡Te pasaste!</h1><br><iframe ALIGN=center width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/-hEt6hUA3rQ\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe><br><form method=\"get\" action=\"/\"><button type=\"submit\">Una oportunidad más</form>")

if __name__ == "__main__":
    app.run()
