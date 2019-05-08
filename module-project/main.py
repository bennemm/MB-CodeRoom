# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:52:16 2019

@author: benne
"""

from list_math import*   
list1 = list(map(int, 
input("Please enter a list of numbers, separated by a space:")
.split()))


def main():
    print (count(list1))
    print(Sum(list1))
    print(average(list1))
    print(Max(list1))
    print(Min(list1))
main()

