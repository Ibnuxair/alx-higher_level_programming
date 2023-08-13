#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    elements_num = len(my_list)
    if elements_num < 0 or idx >= elements_num:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
