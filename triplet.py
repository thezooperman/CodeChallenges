def triplet(arr, n):
    result = 0
    # arr.sort()
    for i in range(len(arr)):
        d = set()
        sum = arr[i]
        for j in range(i + 1, len(arr)):
            complement = abs(sum - arr[j])
            if arr[j] in d:
                result += 1
            d.add(complement)
    return -1 if result == 0 else result


if __name__ == '__main__':
    print(triplet([1, 5, 3, 2], 4))
    # print(triplet([7, 2, 5, 4, 3, 6, 1, 9, 10, 12], 10))
    print(triplet([1, 3, 4, 15, 19], 5))
