#  roman_to_interger.py


import re


def get_value(roman):
    letter_values = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    try:
        return letter_values[roman.upper()]
    except:
        return None


def roman_to_integer(roman):
    regex_pattern = '^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV\
    |V?I{0,3})$'
    is_valid = re.search(regex_pattern, roman)
    assert is_valid is not False, 'Input string is not a valid Roman value'
    assert roman is not "", 'Input string is empty'
    assert roman is not None, 'Input string is not defined'

    last_val = get_value(roman[0])  # start from first value
    assert last_val is not None, 'Invalid roman character'

    res = last_val  # store the last value in result
    for ch in roman[1:]:  # enumerate from 2nd character
        val = get_value(ch)
        if val is None:
            print('Invalid input string - ', roman)
            return
        if val > last_val:
            res += val - 2 * last_val
        else:
            res += val
        last_val = val
    return res


if __name__ == '__main__':
    string = input('Type the Roman value to convert to Integer:').strip()
    print('Roman to Integer:', roman_to_integer(string))
