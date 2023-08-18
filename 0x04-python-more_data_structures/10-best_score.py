#!/usr/bin/python3

def best_score(a_dictionary):
    """
     returns a key with the biggest integer value.
    """

    if a_dictionary is None:
        return (None)

    if len(a_dictionary) == 0:
        return (None)

    max_val = max(a_dictionary.values())
    if max_val == 0 or max_val is None:
        return None

    for key, value in a_dictionary.items():
        if value == max_val:
            return (key)
