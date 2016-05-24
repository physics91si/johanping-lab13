#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import unittest
import calc
import re

class CalcTest(unittest.TestCase):
    # TODO implement tests here to verify that your functions work!
    def testAddition(self):
        self.assertEqual(calc.calc(re.search("\d+\d",s),2))

    def testSubtraction(self):
        self.assertEqual(calc.calc('1-1'), 0)

    def testMultiplciation(self):
        self.assertEqual(calc.calc('1*5'), 5)
 
    def testDivision(self):
        self.assertEqual(calc.calc('10/2'), 5)

    def testSyntax(self):
        with self.assertRaises(SyntaxError):
            calc.calc('+1+1')
            
    def testType(self):
        with self.assertRaises(TypeError):
            calc.calc('string')
        
if __name__ == '__main__': 
    unittest.main()