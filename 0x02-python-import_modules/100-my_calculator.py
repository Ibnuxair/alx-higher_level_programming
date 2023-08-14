#!/usr/bin/python3

from sys import argv
from calculator_1 import add, mul, div, sub

if __name__ == "__main__":
    args_len = len(argv)
    err_msg1 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    err_msg2 = "Unknown operator. Available operators: +, -, * and /"

    if args_len != 4:
        print("{:s}".format(err_msg1))
        exit(1)
    else:
        a = int(argv[1])
        o = argv[2]
        b = int(argv[3])

        if o == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif o == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif o == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif o == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("{:s}".format(err_msg2))
            exit(1)
