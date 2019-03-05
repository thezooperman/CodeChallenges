'''
    Given a string containing digits from 2-9
    inclusive, return all possible letter combinations.
    Skip * and #
    Example:
    fn(23) --> List[str]
    ['ad', 'ae','af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    Extra challenge: print in lexicographic order
'''

from collections import deque

PHONE_PAD = {
    0: ['a', 'b', 'c'],
    1: ['d', 'e', 'f'],
    2: ['g', 'h', 'i'],
    3: ['j', 'k', 'l'],
    4: ['m', 'n', 'o'],
    5: ['p', 'q', 'r', 's'],
    6: ['t', 'u', 'v'],
    7: ['w', 'x', 'y', 'z']
}


def get_phone_pad_recursive_util(results, digits, current, index):
    if len(digits) == index:
        results.append(current)
        return
    letters = PHONE_PAD.get(ord(digits[index]) - ord('2'))
    for l in letters:
        get_phone_pad_recursive_util(results, digits, current + l, index + 1)


def get_phone_pad_recursive(digits: str):
    results = []
    get_phone_pad_recursive_util(results, digits, '', 0)
    return results


def get_phone_digit_combinations(digit: str):
    q = deque()
    sols = []
    if digit:
        q.append('')
        while q:
            node = q.popleft()
            index = len(node)
            if len(node) == len(digit):
                sols.append(node)
                continue
            next_paths = PHONE_PAD.get(ord(digit[index]) - ord('2'))
            print(f'index:{index} next_paths:{next_paths} node:{node}')
            for nc in next_paths:
                q.append(f'{node}{nc}')
    return sols


if __name__ == '__main__':
    print(get_phone_digit_combinations('234'))
    # print(get_phone_pad_recursive('234'))
