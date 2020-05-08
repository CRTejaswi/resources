#!/usr/bin/env python3
from argparse import *
import sys


class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.n = 0

    def __add__(self, numbers):
        n = 0
        return [self.n + i for i in numbers]

    def __sub__(self, numbers):
        n = 0
        return [self.n + i for i in numbers]

    def __mul__(self, numbers):
        n = 0
        return [self.n + i for i in numbers]

    def __div__(self, numbers):
        n = 0
        return [self.n + i for i in numbers]


if __name__ == '__main__':
    parser = ArgumentParser(description='Simple Calculator')
    parser.add_argument('-i', metavar='[INPUT1 [INPUT2] [...]]',
                        action='append',
                        type=int)
    parser.add_argument('-o', metavar='OPERAND',
                        action='store',
                        choices=('+', '-', '*', '/'))
    results = parser.parse_args()
    sys.stdout.write(str(results))
