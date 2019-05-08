# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:16:37 2019

@author: benne
"""

"""
 Program created to receive 5 grades from the user, add the 
 values, and then determine their final grade based on
 following crieteria:
A if sum is greater than or equal to 85
B if sum is greater than or equal to 75 (and less than 85)
C if sum is greater than or equal to 65 (and less than 75)
D if sum is greater than or equal to 50 (and less than 65)
F if sum is less than 50 """

sum =  0

for num in range(5):
    subjectMarks = int(input('Enter your grade (must be between 0 and 20): ')) 
    sum += subjectMarks      
    
if sum >= 85:
    print ("A")
elif sum >= 75:
    print ("B")
elif sum >= 65:
    print ("C")
elif sum >= 50:
    print ("D")
else:
    print ("F")
        
