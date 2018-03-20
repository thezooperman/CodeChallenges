def reverse_brackets(revstr):
    if revstr is None or len(revstr) == 0:
        return 'Can\'t be made balanced using reversals'
    if len(revstr) % 2 != 0:
        return 'Can\'t be made balanced using reversals'
    counter = 0
    s = []
    for b in revstr:
        if b == '}' and len(s) > 0:
            if s[-1] == '{':
                s.pop()
            else:
                s.append(b)
        else:
            s.append(b)
    # all the matching brackets has been identified and closed
    unclosed_bracket = len(s)

    # count the number of open brackets
    while len(s) > 0 and s[-1] == '{':
        s.pop()
        counter += 1
    # return the remaning unclosed brackets + reversed brackets
    return (unclosed_bracket//2) + (counter % 2)


print(reverse_brackets('{{{{'))
print(reverse_brackets('}{{}}{{{'))
print(reverse_brackets('{{{'))
