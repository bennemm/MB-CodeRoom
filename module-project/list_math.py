# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:54:12 2019

@author: benne
"""
'''Math functions that are called in file
main.py '''


def count(list):
    count = len(list)    
    return count
   

def Sum(list):
    s = 0
    for elem in list:
        s+= elem
    return s
    
def average(list):
    n= sum(list)
    d= len(list)
    average = n/d
    return average
    
def Max(list):
    return (max(list))
   

def Min(list1):
    return (min(list))
   
    
