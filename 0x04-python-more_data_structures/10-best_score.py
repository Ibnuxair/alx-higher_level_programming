#!/usr/bin/python3

def best_score(a_dictionary):
    """
     returns a key with the biggest integer value.
    """

    if a_dictionary is None:
        return (None)

    max_val = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_val:
            return (key)
