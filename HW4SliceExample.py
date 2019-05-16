# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:22:37 2019

@author: Ann Marie V. Schilling
"""

# HOW TO GET A SUBSTRING
#This program will print substrings of the value in toSlice
toSlice = "Silver Blue Gold"
rPos = toSlice.find('r')
iPos = toSlice.find('i')

print("Index of the 'i': "+str(iPos))
print("Index of the 'r': "+str(rPos))
print("Note that the slice includes up to, but not including the character at rPos.")
slice = toSlice[iPos:rPos]

print("\nThis is the slice: " +slice)


# HOW TO SEE IF A SLICE IS A PROPER NUMERIC VALUE
# 1.  get the slice
# 2.  if slice contains all digits
# 3.      see if the value is one we want

# EXAMPLE:  We want the value to be between 1000 and 2000
containsNumber = "1234, Can I have a little more?"
#1. get the slice
commaPos = containsNumber.find(',')
numberPart = containsNumber[:commaPos]      # slice from beginning to comma 
print("Number Part: "+str(numberPart))      # let's look at it

#2.  see if it's actually a number
isNumber = numberPart.isdigit()
print("Is it a number?: "+ str(isNumber))

#  How to tell if value is in a range?  Two ways:
r = range(1000,2000)
way1 = int(numberPart) in r

way2 = (1000<= int(numberPart) <= 2000)

print("Is it in the range?: "+str(way1)+" "+str(way2))
