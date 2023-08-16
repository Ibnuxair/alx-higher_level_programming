#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    adds all unique integers in a list (only once for each integer)
    """

    unique_s = set()
    for num in my_list:
        unique_s.add(num)

    result = sum(unique_s)
    return (result)
