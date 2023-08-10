#!/usr/bin/python3
def uppercase(str):
    upper_case = ""
    for ch in str:
        ascii_val = ord(ch)
        if ascii_val >= 97 and ascii_val <= 122:
            upper_ch = chr(ascii_val - 32)
            upper_case += upper_ch
        else:
            upper_case += ch
    print("{:s}".format(upper_case))
