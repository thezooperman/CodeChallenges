# kadane's algo

def maximum_sum(arr):
    cur_win = max_win = 0
    s_index = e_index = 0
    s = 0

    for i in range(len(arr)):
        cur_win += arr[i]
        if max_win < cur_win:
            max_win = cur_win
            s_index = s
            e_index = i

        if cur_win < 0:
            cur_win = 0
            s += 1

    print(f'Max sum: {max_win}, for values: {arr[s_index:e_index + 1]}')


def max_sub_array_of_size_k(k, arr):
    '''
        Given an array of positive numbers and a positive number ‘k’,
        find the maximum sum of any contiguous subarray of size ‘k’.
    '''
    max_win = cur_win = 0
    window = 0
    s = e = 0
    # kadane's algo
    for i in range(len(arr)):
        cur_win += arr[i]
        if i >= k - 1:
            # max_win = max(max_win, cur_win)
            if max_win < cur_win:
                max_win = cur_win
                s = window
                e = i
            cur_win -= arr[window]
            window += 1

    return (max_win, s, e)


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    maximum_sum(arr)
    arr = [2, 1, 5, 1, 3, 2]
    val, s, e = max_sub_array_of_size_k(3, arr)
    print(f'Maximum sum of a subarray of size K: {str(val)} for values: {arr[s:e + 1]}')
    arr = [2, 3, 4, 1, 5]
    val, s, e = max_sub_array_of_size_k(2, arr)
    print(f'Maximum sum of a subarray of size K: {str(val)} for values: {arr[s:e + 1]}')
