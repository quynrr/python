#!/usr/bin/env python3

def simple(seznam):
    for i in range(len(seznam)):
        for j in range(len(seznam) - i -1):
            if seznam[j] > seznam[j+1]:
                temp = seznam[j]
                seznam[j] = seznam[j+1]
                seznam[j+1] = temp
    return seznam 
    
if __name__ == '__main__':
   seznam = [0, -9, 7, 13, -14]
   print(simple(seznam))