#@ cip_chende@yahoo.com
#####################
# 1) Sectiunea documentare modul
#####################
'''
Programul cifre_numar_doc.py

Programul construieste o interfata grafica care ne permite sa tastam un numar
si apoi, la comanda utilizatorului - apasare buton Proceseaza - afiseaza
cifrele numarului de la dreapta la stanga: unitati, zeci, sute etc.

Functia gaseste_cifre_numar este apelata la fiecare apasare a butonului 
'Proceseaza'

Programul stie sa distinga intre numere intregi si text, numere fractionare.
In cazul in care valoarea introdusa nu este un intreg se afiseaza o eroare.
'''

#####################
# 2. Sectiunea import
#####################
import tkinter


#####################
# 3. Sectiunea functii procesare specifice aplicatiei ('business logic')
#####################
def gaseste_cifre_numar(numar, loc_afisare):
    '''
    Functie care determina cifrele dintr-un numar si le afiseaza in 'loc_afisare'
    Cifrele sunt citite de la dreapta la stanga adica: unitati, zeci, sute ...
    
    Parametrii:
        numar:          valoarea pe care o analizam. Daca este un intreg se 
                        afiseaza cifrele
                        
        loc_afisare:    wiget-ul (componenta grafica) unde se afiseaza rezultatul    
    '''
    i = 1
    ret = ""
    print("DBG: numar = ", numar)
    # Tratare erori. Verificam daca valoarea primita este numar
    try:
        numar = int(numar)
    except Exception as e:               # Exceptia in acest caz este ValueError
        print("DBG: ", e.__class__.__name__, e)
        ret = "\nValoare introdusa: '" + numar + "' Nu este un numar intreg."
        ret += "\nIntroduceti un numar si apoi apasati butonul 'Proceseaza'"
        loc_afisare["text"] = ret
        return ret
        
    ret = "Cifre numar (unitati, zeci ...):\n"
    while numar > 0:
        uc = numar % 10
        numar = numar // 10
        ret += str(i) + ": " + str(uc) + "\n"
        i += 1
        
    loc_afisare["text"] = ret
    return ret
            
            

#####################
# 4. Sectiunea construire aplicatie grafica
#####################
app = tkinter.Tk()

# configurare titlu fereastra
app.wm_title("Cifre numar")


'''
Definire componente aplicatie aplicatie:
 - o componenta de tip Entry - pentru a introduce text
 - o componenta de tip Buton - pentru a executa codul al carui rezultat vrem
                             sa-l afisam 
 - o componenta de tip Label - pentru a afisa rezultatul procesarii
'''
app_numar = tkinter.Entry(app)
app_buton = tkinter.Button(app, text="Proceseaza", \
    command = lambda: gaseste_cifre_numar(app_numar.get(), app_rezultat))
app_rezultat = tkinter.Label(app, text="rezultat")


# Afisare componente grafice
app_numar.grid(row = 0, column = 0)
app_buton.grid(row = 0, column = 1)
app_rezultat.grid(row = 1, column = 0, columnspan=2)

# Pornire bucla evenimente - aplicatia asteapta comenzi de la utilizator
if __name__ == '__main__':
    app.mainloop()


