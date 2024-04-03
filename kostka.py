#!/usr/bin/env python3 

import random
import bubblesort 

class Kostka:
    def __init__(self, pocetSten=6):
        self.pocetSten = pocetSten

    def hod(self):
            return random.randint(1, self.pocetSten)


if __name__ == "__main__":

    k1 = Kostka()
    k2 = Kostka(12)
    k3 = Kostka(10)

    print(k2.hod())
    print(k1.hod())
    print(k3.hod())
    pole = [9,4,5,7,1,3]
    print(bubblesort.simple(pole))