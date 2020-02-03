def compress(string):
    count = 1
    prev = string[0]
    result = []
    for idx, cur in enumerate(string[1:]):
        if cur != prev or idx + 1 == len(string):
            if count > 1:
                result.append(f'{prev}{count}')
                count = 1
            else:
                result.append(f'{prev}')
            prev = cur
        else:
            count += 1
    if count > 1:
        result.append(f'{cur}{count}')
    else:
        result.append(f'{cur}')
    compressed = ''.join(result)
    return compressed if len(compressed) < len(string) else string

def compress_inplace(string):
    anchor = write = 0
    string = list(string)
    for read, char in enumerate(string):
        if read + 1 == len(string) or char != string[read + 1]:
            string[write] = string[anchor]
            write += 1
            if read > anchor:
                for j in str(read - anchor + 1):
                    string[write] = j
                    write += 1
            anchor = read + 1
    return ''.join(string)

print(compress('aaabc'))
print(compress('abc'))
print(compress_inplace('aaabbc'))