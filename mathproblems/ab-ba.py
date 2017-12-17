#!/usr/local/bin/python
import time
import sys
import logging

SquareNumbers = []

def GenerateSquareNumbers():
    for i in range(101):
        SquareNumbers.append(i*i)

GenerateSquareNumbers()

#for value in SquareNumbers:
#    sys.stdout.write("Value is %d\n" % value)

def isSquareNumber(a):
    for value in SquareNumbers:
        if a == value:
            return True
    return False

count = 0
for A in range(1,10):
    for B in range(1,10):
            result = 10*A + B  - (10*B + A)
            if (isSquareNumber(result)):
                sys.stdout.write("%d%d - %d%d = %d\n" % (A,B,B,A,result))
                count = count + 1
sys.stdout.write("count = %d\n" % count)


