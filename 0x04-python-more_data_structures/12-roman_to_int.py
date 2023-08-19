#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    converts a Roman numeral to an integer
    """

    if isinstance(roman_string, str) and roman_string is not None:
        roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        result = 0
        prev_result = 0
        for c in reversed(roman_string):
            value = roman_numerals.get(c, 0)
            if value >= prev_result:
                result += value
            else:
                result -= value
            prev_value = value
        return (result)
    return (0)
