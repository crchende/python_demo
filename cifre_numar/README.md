Exemplu program cu interfata grafica
=====================================

![image](https://user-images.githubusercontent.com/57460107/232603434-bea98de3-903b-4670-afc7-bbf5cac2593d.png)

Programul primeste ca intrare un numar si-i afiseaza cifrele, de la dreatpta la stanga: unitati, zeci sute ...
Algoritmul va fi implementat in C/C++ si Python. Pe langa algoritm, vom adauga si interfata grafica in doua variante:
* ferestre specifice sistemului de operare folosit (windows, Mac, Linux) folosind biblioteca *tkinter;
* interfata WEB, vizualizare rezultatului executie algoritmului in browser si preluare numar de prelucrat din URL - folosind framework-ul *flask

__*NOTA: Programele au fost testate pe Ubuntu 20.04.__

### Descrie algoritm gasire cifre
Pornim de la un algoritm studiat in general in liceu: am un numar (ex 123) si vreau sa vad ce cifre am in numar (ex: 3, 2, 1).
Algoritmul contine urmatorii pasi:
1) am numarul
    - fie citit de la tastatura (cin >> nr;)
    - fie dat in program (int nr = 123;)
    - fie dat ca parametru in linia 

2) folosim o bucla while:
    - cat timp numar > 0
      - ultima_cifra = numar % 10
      - afiseaza ultima_cifra
      - numar = numar / 10


## Variante implementare

### 1) C/C++
Codul este in fisierul __cifre_numar.cpp__.

Pe linux acesta poate fi compilat folosind comanda:
__g++ -o cifre_numar cifre_numar.cpp__
care trebuie executata din directorul in care se afla fisierul cifre_numar.cpp

In urma compilarii va rezulta fisierul executabil: __cifre_numar__.
Programul nu are interfata grafica, poate fi executat din terminal si asteapta ca parametru numarul care trebuie procesat.

### 2) cifre_numar_cpp.py
Programul Python creaza interfata grafica. Aceasta contine:
 - un element grafic (widget) de tip 'Entry', care ne permite sa scriem in el;
 - un element grafic de tip 'Button' cu care pornim procesarea dupa ce am introdus datele in 'Entry'
 - un element grafic de tip 'Label' in care vom afisa rezultatul procesarii.

La apasarea pe butonul Proceseaza, programul preia continutul elementului grafic 'Entry' si apeleaza fisierul executabil rezultat in urma compilarii programului cifre_numar.cpp, dandu-i ca parametru ce a citit din Entry:
__cifre_numar \<date luate in Entry\>__

Ceea ce afiseaza executabilul __cifre_numar__ (output-ul) este preluat de Python si afisat in elementul "Label" din interfata grafica.
    
### 3) cifre_numar.py
Atat partea de gasire cifre numar cat si partea grafica sunt scrise in Python.
Programul contine minimul de cod necesar pentru interfata grafica si pentru algoritm. Nu face tratarea erorilor nici partea de documentare a codului.
Are aproximativ 30 de linii de cod.

Exemplu lansare in executie:

![image](https://user-images.githubusercontent.com/57460107/233189359-4a5d1b43-7311-43e3-b01d-1b0db4dfb003.png)

*NOTA - la fel se lanseaza in executie si celelalte programe python, cu comanda: __python3 \<nume fisier .py\>__*

### 4) cifre_numar_doc.py
Aceasta varianta include si partea de tratare erori si de documentare a codului.
Ca dimensiune este de aproximativ 90 de linii de cod.

*!!! ___de retinut__ - dimensiunea unui cod complet - cu tratare erori si documentare - chiar si pentru o aplicatie foarte simpla este de cel putin 3 ori mai mare decat varianta functionala minima a unui program. Pentru a face un produs, bun de livrat si utilizat efortul poate fi chiar de 10+ ori mai mare decat varianta minima functionala (__MVP__ Minimum Viable Product)*

### 5) cifre_numere_web.py
Programul implementeaza acelasi algoritm ca si programele anterioare doar ca utilizeaza framework-ul *flask* pentru a afisa rezultatul executiei in browser si pentru a prelua datele de la utilizator din browser (din URL).

Imaginile de mai jos contin exemple de lansare in executie a programului, pagina principala, si pagina care afiseaza rezultatele:

![image](https://user-images.githubusercontent.com/57460107/233188316-cebdcbf0-74d1-470b-9500-114e7da0460c.png)

![image](https://user-images.githubusercontent.com/57460107/233188732-4281c36c-aff1-41c1-b4d7-86a47d887297.png)

![image](https://user-images.githubusercontent.com/57460107/233188565-b682c1f0-4ff6-4582-9d37-6c484eca04a2.png)




