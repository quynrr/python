#!/usr/bin/env python3

morse = {'a':'·−', 'b':'−···', 'c':'−·−·', 'd':'−··', 'e':'.', 
        'f':'··−·', 'g':'−−·', 'h':'····', 'i':'··', 'j':'·−−−', 
        'k':'−·−', 'l':'·−··', 'm':'−−', 'n':'−·', 'o':'−−−', 
        'p':'·−−·', 'q':'−−·−', 'r':'·−·', 's':'···', 't':'−', 
        'u':'··−', 'v':'···−', 'w':'·−−', 'x':'−··−', 
        'y':'−·−−', 'z':'−−··', ' ':''}

def preloz():
    vstup = input('zadej text:')

    for pismeno in vstup:
        try:
            print(morse[pismeno.lower()] + '/', end='')
        except:
            print('?/', end='')

    print('//')

if __name__ == '__main__':
    preloz()
