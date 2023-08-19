#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple (<score>, <weight>)
    """

    if len(my_list) == 0:
        return 0

    summation = total_weight = 0

    for score, weight in my_list:
        summation += score * weight
        total_weight += weight

    return summation / total_weight
