def complement():
    nums = [[4, 2], [3, 4]]

    def inner(val):
        x, y = val[0], val[1]
        count = {}
        final = []
        for i, num in enumerate(range(x)):
            complement = x - num - 1
            if complement in count:
                if (complement + num + 1) == x and\
                        (complement ^ (num + 1)) == y:
                    final.append((complement, num + 1))
            count[num + 1] = i + 1
        if len(final) == 0:
            return -1
        else:
            return min(final)
    for i, val in enumerate(nums):
        res = inner(val)
        print(res)
        if i == 0:
            assert res == (1, 3)
        else:
            assert res == -1


def uniquesubset_recursive():
    nums = [4, 5, 6, 4, 5]
    fin_set = set()

    def inner(nums, current, position, fin_set):
        if position < 0:
            fin_set.add(' '.join(str(c) for c in current))
            return
        # include current element
        current.append(nums[position])
        inner(nums, current, position - 1, fin_set)
        # ignore last selected element
        current.pop(-1)
        # remove duplicate elements
        # while position > 0 and nums[position] == nums[position - 1]:
        #     position -= 1
        # exclude current element
        inner(nums, current, position - 1, fin_set)
        return fin_set
    return inner(sorted(nums), [], len(nums) - 1, fin_set)


def uniquesubset_iterative():
    nums = [4, 5, 6, 4, 5]
    digit_length = len(nums)
    fin_set = set()
    bin_combinations = pow(2, digit_length)
    nums = sorted(nums)
    for bin_iter in range(bin_combinations):
        tmp_str = ' '.join([str(nums[bit]) for bit in range(
            digit_length) if (bin_iter & (1 << bit))])
        fin_set.add(tmp_str)
    return fin_set


def permutations(head, tail=''):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail + head[i])


def string_permutation_2(string, k=0):
    if k == len(string):
        print(*string)
    else:
        for i in range(k, len(string)):
            string[k], string[i] = string[i], string[k]
            string_permutation_2(string, k + 1)
            string[k], string[i] = string[i], string[k]


if __name__ == '__main__':
    complement()
    x = complement
    subset = uniquesubset_recursive()
    assert len(subset) == 18
    print(subset)
    subset = uniquesubset_iterative()
    assert len(subset) == 18
    print('\n')
    print(subset)
    permutations('stop')
    # string_permutation_2(['s', 't', 'o', 'p'])
