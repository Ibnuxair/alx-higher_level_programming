#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for i in range(1, 5):
        my_list.append(i)

    for j in range(5):
        print("{:d}".format(my_list[j]))