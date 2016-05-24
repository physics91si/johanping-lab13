#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import sys
import string
import re

def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    calculation = ''.join(sys.argv[1:])
    print(calc(calculation))

def calc(s):
    """Parse a string describing an operation on quantities with units."""

    
    # TODO make this robust for differently formatted inputs
        
    numbers = []
    numbers = s.split("([+-/*])",s)
    print(list(numbers))
    
    num1 = s[0]
    num2 = s[2]
    operation = s[1]

    if operation=='+':
        return int(num1)+int(num2)
    elif operation=='-':
        return int(num1) - int(num2)
    elif operation=='*':
        return int(num1)*int(num2)
    elif operation=='/':
        return int(num1)/int(num2)
    
    

if __name__ == "__main__": main()
