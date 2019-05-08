# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:10:13 2019

@author: benne
"""

f= open('myfile.txt', 'w')

l= ['hi', 'there', 'I', 'am', 'writing', 'in', 'a', 'file']

with open('myfile.txt', 'w') as f:
    for s in l:
        f.write(s +'\n')

with open('myfile.txt', 'r') as f:
    for line in f:
        print(line, end='')
        
with open('myfile.txt', 'a') as f:
        f.write('Bye\n')

import os
os.remove('myfile.txt')