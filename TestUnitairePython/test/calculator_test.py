# test Unit Calculator

import unittest
import sys
sys.path.append('')

from classScript import Calculator

class TestCalculator(unittest.TestCase):

    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the secod number : "))

    def test_values(num1, num2):
        if num1 and num2 is not int:
            return False
        else:
            return True

    def test_add(self):
        if self.test_values:
            result = Calculator.add(self.num1, self.num2)

    def test_subtract(self):
        if self.test_values:
            result = Calculator.subtract(self.num1, self.num2)

    def test_multiply(self):
        if self.test_values:
            result = Calculator.multiply(self.num1, self.num2)

    def test_divide(self):
        if self.test_values:
            result = Calculator.divide(self.num1, self.num2)

    def test_power(self):
        if self.test_values:
            result = Calculator.power(self.num1, self.num2)

    def test_square_root(self):
        if self.test_values:
            result = Calculator.square_root(9)

    operation = input("Enter the operation you would like to perform (add, subtract, multiply, divide, square_root, power): ")

    print(Calculator.calculate(operation, num1, num2))