#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args_len = len(sys.argv)
    i = 1
    result = 0

    if args_len == 1:
        print("{:d}".format(result))
    else:
        while i < args_len:
            result += int(sys.argv[i])
            i += 1
        print("{:d}".format(result))
