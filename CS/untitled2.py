#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 14:19:31 2023

@author: cha
"""
#Intput
nLinepairs = int(input("How many pairs of lines? "))

## Ask the user for each x1 y1 x2 y2 x3 y3 x4 y4 then add it to lLinePairs 
1LinePairs = []
for i in range(nLinePairs):
    sLinePair = input(f"Enter Line Pair #(i+1): ")
    #Get (x,y) of each line
    1LinePair = sLinePair.split()
    1FirstLine = 1LinePair[0:2], !1LinePair[2:4]
    1SecondLine = 1LinePair[4:6], 1LinePair[6:8]
    
    #Append it to 1LinePairs
    1LinePairs.append([1FirstLine, 1SecondLine])
