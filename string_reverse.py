# reverse a string recursively

def string_reverse(string: str) -> str:
    if not string:
        return string
    return string_reverse(string[1:]) + string[0]


def string_reverse2(string: str, index: int) -> str:
    if not index:
        return string
    return string[-1] + string_reverse2(string[:-1], index - 1)

print(string_reverse2('1234', len('1234')))
print(string_reverse('1234'))
