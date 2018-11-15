#code
from collections import deque

def merge_int(intervals):
    stack = deque()
    for elem in intervals:
        if len(stack) == 0 or elem[0] > stack[-1][1]:
            stack.append(elem)
        if stack[-1][1] < elem[1]:
            stack[-1][1] = elem[1]
    return ''.join(' '.join(str(i[0]) + ' ' + str(i[1]) for i in stack))


if __name__ == '__main__':
    test_cases = int(input())
    output = []
    for tc in range(test_cases):
        no_of_int = int(input())
        intervals = list(map(int, input().strip().split(' ')))
        if (len(intervals) // 2) != no_of_int:
            break
        arr = []
        for elem in range(-1, len(intervals) - 1, 2):
            arr.append([intervals[elem + 1], intervals[elem + 2]])
        arr = sorted(arr)
        output.append(merge_int(arr))
    for res in output:
        print(res)