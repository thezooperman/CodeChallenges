"""
Problems:
    1. Given an integer number, convert it to roman
    2. Given a roman numeral, convert it to integer
"""

import re


def get_value(roman: str) -> int:
    letter_values = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'V': 5,
        'I': 1
    }
    try:
        return letter_values[roman.upper()]
    except:
        return None


def integer_to_roman(integer: int) -> str:
    if integer < 1 or integer > 3999:
        raise ValueError('Invalid numeral passed. Cannot be converted to roman.')
    return_val = []
    lv_index = 0

    denominations = [1000, 500, 100, 50, 10, 5, 1]
    literals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    letter_values = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'V': 5,
        'I': 1
    }

    result = ""
    for (roman, arabic) in letter_values.items():
        (factor, integer) = divmod(integer, arabic)
        result += roman * factor
    return result


def roman_to_integer(roman: str) -> int:
    regex_pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    is_valid = re.search(regex_pattern, roman)
    assert is_valid is not None, 'Input string is not a valid Roman value'
    assert roman != "", 'Input string is empty'
    assert roman is not None, 'Input string is not defined'

    res = get_value(roman[-1])
    for i in range(len(roman) - 2, -1, -1):
        if roman[i] >= roman[i + 1]:
            res -= get_value(roman[i])
        else:
            res += get_value(roman[i])
    return res


if __name__ == '__main__':
    string = input('Type the Roman value to convert to Integer:').strip()
    print('Roman to Integer:', roman_to_integer(string))

    string = input('Type the integer value to convert to Roman:').strip()
    print('Integer to Roman:', integer_to_roman(int(string)))
