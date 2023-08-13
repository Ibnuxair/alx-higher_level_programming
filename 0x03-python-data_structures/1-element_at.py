#!/usr/bin/python3

def element_at(my_list, idx):
    elements_num = len(my_list)
    if idx < 0 or idx >= elements_num:
        return
    else:
        return (my_list.pop(idx))
