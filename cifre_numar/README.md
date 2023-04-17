Exemplu program cu interfata grafica
=====================================
Adaugare interfata grafica - fereastra specifica sistemului de operare Linux/Windows/Mac si interfata WEB unui program care afiseaza cifrele dintr-un numar.
Avem programul __cifre_numar__ rezultat in urma compilarii programului __cifre_numar.cpp__

* NOTA: Programele au fost testate pe Ubuntu 20.04.

Pe linux, compilarea se face cu comanda:
__g++ -o cifre_numar cifre_numar.cpp__
care trebuie executata din directorul in care se afla fisierul cifre_numar.cpp

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

### Adaugare interfata grafica - fereastra specifica sistemului de operare(Windows / Linux / Mac)
#### cifre_numar_cpp.py
- 



