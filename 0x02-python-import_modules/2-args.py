#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_len = len(sys.argv)
    i = 1

    if args_len == 1:
        print("{:d} arguments.".format(args_len - 1))
    elif args_len == 2:
        print("{:d} argument:".format(args_len - 1))
        print("{:d}: {:s}".format(args_len - 1, sys.argv[args_len - 1]))
    else:
        print("{:d} arguments:".format(args_len - 1))
        while i < args_len:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
