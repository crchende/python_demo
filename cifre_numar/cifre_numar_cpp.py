#@ cip_chende@yahoo.com
import tkinter
import subprocess

def gaseste_cifre_numar(numar, loc_afisare):
    i = 1
    ret = ""
    # tratare erori - valoare primita NU este intreg:
    print("DBG: numar = ", numar)
        
    ret = subprocess.getoutput(f"./cifre_numar {numar}")        
            
    loc_afisare["text"] = ret
    return ret

#############
app = tkinter.Tk()
app.wm_title("Cifre numar")

app_numar = tkinter.Entry(app)
app_buton = tkinter.Button(app, text="Proceseaza", \
    command = lambda: gaseste_cifre_numar(app_numar.get(), app_rezultat))
app_rezultat = tkinter.Label(app, text="rezultat")

app_numar.grid(row = 0, column = 0)
app_buton.grid(row = 0, column = 1)
app_rezultat.grid(row = 1, column = 0, columnspan=2)

app.mainloop()


