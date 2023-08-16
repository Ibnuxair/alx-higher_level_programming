def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary with ordered keys.
    """
    sorted_keys = sorted(a_dictionary)

    for key in sorted_keys:
        value = a_dictionary[key]
        print(key, value)
