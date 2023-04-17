//@ cip_chende@yahoo.com
#include <iostream>
#include <string.h>
using namespace std;

/*
 Programul primeste parametrii in linia de comanda.
 Numarul acestora este in contorul argc
 Valorile sunt in vectorul de siruri: argv
*/

int main(int argc, char *argv[]) {
    int nr, i, uc;
    
    //Vefificam daca programul este apelat corect
    //In caz de apel incorect, se afiseaza un mesaj care indica apelul corect
    if(argc != 2) {
        cout << endl << "Utilizare:" << endl;
        cout << "cifre_numar <numar>" << endl << endl;
        return 1;
    }
    
    //conversie din sir in numar. Parametrii din linia de comanda sunt siruri
    nr = atoi(argv[1]); //functie din string.h 'ansi string to integer'
    
    cout << "Numarul dat ca parametru: " << nr << endl;
    
    while(nr > 0) {
        uc = nr % 10;
        cout << "cifra: " << uc << endl;
        nr = nr / 10;
    }
    
    return 0;
}
