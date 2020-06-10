from typing import List


def sequence(arr: List[str]) -> List[int]:
    if not arr:
        return []

    initial = 0
    i = 1
    l = len(arr)
    first_char = arr[initial]
    return_list = []
    found = False
    counter = -1
    more_occurence = False

    while i <= l:
        j = l - 1

        # if matching string found in subset
        more_occurence = first_char in arr[i + 1:]

        if more_occurence:
            while j > i:
                if arr[j] == first_char:
                    found = True
                    break
                j -= 1

            if found:
                count = j - initial + 1
                return_list.append(count)
                i, j = j, 0

                if i < (l - 1) or (i + 1) < (l - 1):
                    initial = i + 1
                    first_char = arr[initial]
        elif not found:
            return_list.append(1)
        elif found:
            counter += 1

        i += 1
    if counter > 0:
        return_list.append(counter)

    return return_list


input_str = ["a", "b", "c", "a", "b", "c", "a", "e", "f", "g", "h", "e"]
output = [7, 5]

print(sequence(input_str))


input_str = ["a", "b", "c"]
output = [1, 1, 1]

print(sequence(input_str))


input_str = ["z", "z", "c", "d", "e", "z", "a", "c", "f", "c", "h", "i"]
output = [6, 6]

print(sequence(input_str))
