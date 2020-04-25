text_input = input('\nWprowadź tekst >   ')
klucz_input = int(input('\nWprowadź klucz do szyfrowania - liczba w przedziale [0....255] >   '))

def zaszyfruj(tekst, klucz):
    
    def dodawanie_zer(argument):
        if len(argument) < 8:
            argument = ['0'] * (8 - len(argument)) + argument
        return argument
    
    lista_liter = list(tekst)
    dlugosc_wyrazu = int(len(lista_liter))
    
    for i in range(dlugosc_wyrazu):
        lista_liter[i] = dodawanie_zer(list(bin(int(ord(str(lista_liter[i]))))[2:]))
    
    klucz = dodawanie_zer(list(bin(int(klucz))[2:]))
    
    for i in range(dlugosc_wyrazu):
        for j in range(len(lista_liter[i])):
            if lista_liter[i][j] == klucz[j]:
                lista_liter[i][j] = '0'
            else:
                lista_liter[i][j] = '1'
        lista_liter[i] = chr(int((''.join(lista_liter[i])),2))

    zaszyfrowany_wyraz = ''.join(lista_liter)
    
    return zaszyfrowany_wyraz

print('\n','Wprowadzony tekst zaszyfrowany za pomocą algorytmu "XOR" to: ',zaszyfruj(text_input, klucz_input),'\n')