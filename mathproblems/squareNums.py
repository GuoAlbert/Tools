#!/usr/local/bin/python
import time
import sys
import logging

result = 0

def Calculate():
    result = 0
    for i in range(1,10):
        result = result + (i) * (i)
    sys.stdout.write("result = %d\n" % result)


Calculate()



