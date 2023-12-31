#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    modified_tuple_a = modify_tuple(tuple_a)
    modified_tuple_b = modify_tuple(tuple_b)

    sum_tuple = (modified_tuple_a[0] + modified_tuple_b[0],
                 modified_tuple_a[1] + modified_tuple_b[1])
    return (sum_tuple)


def modify_tuple(tuple_data):
    if len(tuple_data) == 0:
        return (0, 0)
    elif len(tuple_data) == 1:
        return (tuple_data[0], 0)
    else:
        return (tuple_data[0], tuple_data[1],)
