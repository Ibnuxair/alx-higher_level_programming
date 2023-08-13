#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    elements_len = len(my_list)
    if idx < 0 or idx >= elements_len:
        return (my_list)
    else:
        copied_list[idx] = element
        return (copied_list)
