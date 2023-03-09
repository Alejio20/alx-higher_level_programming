#!/usr/bin/python3
"""The program imports all functions from the file calculator_1.py
    and handles basic operations
"""
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    count = len(sys.argv) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = sys.argv[1]
        operator = sys.argv[2]
        b = sys.argv[3]

        if operator == "+":
            print("{} + {} = {}".format(a, b, int(add(a, b))))
        elif operator == "-":
            print("{} - {} = {}".format(a, b, int(sub(a, b))))
        elif operator == "*":
            print("{} * {} = {}".format(a, b, int(mul(a, b))))
        elif operator == "/":
            print("{} / {} = {}".format(a, b, int(div(a, b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
