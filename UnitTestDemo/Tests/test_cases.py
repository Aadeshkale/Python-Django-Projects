from unittest import TestCase
from Mymath.Mathop import math

class test_math(TestCase):
    def setUp(self):
        self.m=math()
        print('Setup is created')
    def tearDown(self):
        del self.m
        print('tear down')

    def test_add(self):
        print('Add function Tested')
        self.assertTrue(self.m.add(15,12)==27)
        self.assertTrue(self.m.add(5, -3)==2)


    def test_mul(self):
        print('Function Multiplication Tested ')
        self.assertTrue(self.m.mul(2,2)==4)
        self.assertTrue(self.m.mul(2,3)==6)


    def test_sub(self):
        print('Function Substraction Tested')
        self.assertTrue(self.m.sub(12,2)==10)
        self.assertTrue(self.m.sub(-2, -2)== 0)

    def test_div(self):
        print('Function Division Tested')
        self.assertTrue(self.m.div(25,25)==1.0)
        self.assertTrue(self.m.div(4,2)==2.0)
