import itertools

string = input().strip()

[print('(%s, %s) ' % (len(list(cgen)), c), end='')for c, cgen \
    in itertools.groupby(string)]
