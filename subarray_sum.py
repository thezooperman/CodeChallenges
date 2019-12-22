from collections import defaultdict


def subarray_sum(arr, s):
    if not arr or not s:
        raise TypeError('Bad shit!')

    start = 0
    cur_sum = arr[0]
    i = 1

    while i <= len(arr):
        while cur_sum > s and start < i - 1:
            cur_sum -= arr[start]
            start += 1

        if cur_sum == s:
            print(start + 1, i)
            return

        if i < len(arr):
            cur_sum += arr[i]
        i += 1
    print(-1)


def insert_record(map, sum_so_far, index):
    if not map.get(sum_so_far):
        map[sum_so_far] = []
    map[sum_so_far].append(index + 1)


def subarr_2(arr, s):
    sum_so_far = 0
    map = {}
    foundMatch = False

    map[0] = []
    map[0].append(-1)
    for i, v in enumerate(arr):
        sum_so_far += v
        if (sum_so_far - s) in map:
            foundMatch = True
            print_stuff = map.get(sum_so_far - s)
            for pr in print_stuff:
                print(pr, end=' ')

        insert_record(map, sum_so_far, i)
    if not foundMatch:
        print(-1)


if __name__ == '__main__':
    subarr_2([1, 2, 3, 7, 5], 12)
    print(flush=True)
    subarray_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
    # subarray_sum([135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162,
    #               92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117,
    #               119,
    #               96, 48, 127,
                #   172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134], 468)
