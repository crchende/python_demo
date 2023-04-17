#@ cip_chende@yahoo.com
from flask import Flask, escape

def gaseste_cifre_numar(numar):
    i = 1
    ret = ""
    # tratare erori - valoare primita NU este intreg:
    print("DBG: numar = ", numar)
    numar = int(numar) # valoarea citita din interfata grafica este 'string'
        
    ret = "Cifre numar (unitati, zeci ...):<br>"
    while numar > 0:
        uc = numar % 10
        numar = numar // 10
        ret += "cifra " + str(i) + ": " + str(uc) + "<br>"
        i += 1
        
    return ret

app = Flask(__name__)

@app.route('/')
def index():
    ret = "<h1>Cifre Numere</h1>"
    ret += "Adaugati un numar la URL si apasati pe ENTER<br>"
    ret += "Ex<br>"
    ret += "http://127.0.0.1:5001/345<br>"

    return ret

@app.route('/<numar>')
def cifre_numar(numar):
    numar = escape(numar)
    return gaseste_cifre_numar(numar)
    
    
app.run(host = "127.0.0.1", port = 5001)
