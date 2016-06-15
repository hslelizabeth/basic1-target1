# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:50:40 2016

@author: Elizabeth
"""

a = [8,2,4,6,1,9,0,3,5,7]
b = 0
la = len(a)
for j in range(1,len(a)-2):
    for i in range(0,len(a)-j):
        if a[i] < a[i+1]:
            b = a[i]
            a[i] = a[i+1]
            a[i+1] = b
        else:
            continue
print (a)