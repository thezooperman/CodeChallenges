#!/usr/bin/env python3


def edit_distance_calculate(string_A: str, string_B: str) -> bool:
    '''
        Strings cannot mismatch by more than 1 units
        Edit distance cannot be more than 1
        Args:
            string_A type: str
            string_B type: str
            return type: bool
    '''
    len_A, len_B = len(string_A), len(string_B)

    if abs(len_A - len_B) > 1:
        return False

    if string_A == string_B:
        return True

    distance = 0

    if len_A == len_B:
        for i in range(len_A):
            if string_B[i] != string_A[i]:
                distance += 1
                if distance > 1:
                    return False
        return True
    else:
        if len_A > len_B:
            short_string = string_B
            long_string = string_A
        else:
            short_string = string_A
            long_string = string_B
        # run a possible string combination and
        # match with short string
        for i in range(len(long_string)):
            temp = long_string[:i] + long_string[i + 1:]
            if temp == short_string:
                return True
        return False


if __name__ == '__main__':
    var_a, var_b = 'aaa', 'aaaa'
    print(
        f'Edit distance for {var_a}, {var_b}: {edit_distance_calculate(var_a, var_b)}')
    var_a, var_a = 'aaa', 'aaaaa'
    print(
        f'Edit distance for {var_a}, {var_b}: {edit_distance_calculate(var_a, var_b)}')
    var_a, var_b = 'aaa', 'aaab'
    print(
        f'Edit distance for {var_a}, {var_b}: {edit_distance_calculate(var_a, var_b)}')
    var_a, var_b = 'aaa', 'bbbb'
    print(
        f'Edit distance for {var_a}, {var_b}: {edit_distance_calculate(var_a, var_b)}')
    var_a, var_b = '', ''
    print(
        f'Edit distance for {var_a}, {var_b}: {edit_distance_calculate(var_a, var_b)}')
    var_a, var_b = 'aaaa', 'aaba'
    print(
        f'Edit distance for {var_a}, {var_b}: {edit_distance_calculate(var_a, var_b)}')
    var_a, var_b = 'aaaa', 'babb'
    print(
        f'Edit distance for {var_a}, {var_b}: {edit_distance_calculate(var_a, var_b)}')
