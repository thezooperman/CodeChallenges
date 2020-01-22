# reverse a string recursively

def string_reverse(string: str) -> str:
    if not string:
        return string
    return string_reverse(string[1:]) + string[0]


def string_reverse2(string: str, index: int) -> str:
    if not index:
        return string
    return string[-1] + string_reverse2(string[:-1], index - 1)

def string_reverse3(string: str) -> str:
    return ''.join(_ for _ in string[::-1])

def string_reverse4(string : str, length: int) -> str:
    string = list(string)
    for i in range(0, length // 2):
        string[i], string[length - i - 1] = string[length - i - 1], string[i]
    return ''.join(string)

print(string_reverse2('1234', len('1234')))
print(string_reverse('1234'))
print(string_reverse3('stop'))
print(string_reverse4('bald', 4))