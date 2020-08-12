from typing import List

"""
    Given a sorted array arr[] and a number x, write a function that
    counts the occurrences of x in arr[].
    Expected time complexity is O(Logn)

    Examples:

        Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
        Output: 4 // x (or 2) occurs 4 times in arr[]

        Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
        Output: 1

        Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
        output: 4

        Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
        Output: -1 // 4 doesn't occur in arr[]
"""


def right(arr: List[int], search_key: int, low: int, high: int) -> int:
    if low > high:
        return low
    mid = (low + high) // 2

    if arr[mid] > search_key:
        return right(arr, search_key, low, mid - 1)
    else:
        return right(arr, search_key, mid + 1, high)


def left(arr: List[int], search_key: int, low: int, high: int) -> int:
    if low > high:
        return low
    mid = (low + high) // 2

    if arr[mid] < search_key:
        return left(arr, search_key, mid + 1, high)
    else:
        return left(arr, search_key, low, mid - 1)


def occurrence_count() -> None:
    # int_arr = [1, 1, 2, 2, 2, 2, 3]
    # key = 2
    int_arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    key = 5
    left_index = left(int_arr, key, 0, len(int_arr) - 1) + 1
    right_index = right(int_arr, key, 0, len(int_arr) - 1)
    print("Key: {} -Left Index:{} Right Index:{} Total occurrence:{}"
          .format(key,
                  left_index,
                  right_index,
                  right_index - left_index + 1))
    assert left_index == 2
    assert right_index == 4
    assert (right_index - left_index + 1) == 3


"""
    Find the transition point in a binary array.
    Given a sorted array containing only numbers 0 and 1, the task is to
    find the transition point efficiently.
    The transition point is a point where “0” ends and “1” begins.
    
    Examples :

        Input: 0 0 0 1 1
        Output: 3

        Explanation: Index of first 1 is 3

        Input: 0 0 0 0 1 1 1 1
        Output: 4

        Explanation: Index of first 1 is 4
"""


def first_non_zero(arr: List[int], low: int, high: int) -> int:
    if low > high:
        return low
    mid = (low + high) // 2
    if arr[mid] < 1:
        return first_non_zero(arr, mid + 1, high)
    else:
        return first_non_zero(arr, low, mid - 1)


def one_sided_search():
    int_arr = [0, 0, 0, 0, 1, 1, 1, 1]
    low, high = 0, len(int_arr) - 1
    get_non_zero_index = first_non_zero(int_arr, low, high)
    print(get_non_zero_index)
    assert get_non_zero_index == 4, "Expected index is 4"


def square_root_search(n: int, precision: int) -> float:
    ans, low, high = 1, 1, n
    mid_flag = False
    while low <= (high // 2):
        mid = int(low + (high - low)) / 2
        if (mid * mid) == n:
            ans = mid
            mid_flag = True
            break
        if (mid * mid) < n:
            low = mid + 1
        else:
            high = mid - 1

    if not mid_flag:
        ans = low

    increment = 0.1
    for i in range(precision):
        while ans * ans <= n:
            ans += increment

        ans -= increment
        increment /= 10
    return round(ans, precision)

def find_nth_root(x:int, n: int) -> float:
    x = float(x)
    n = int(n)

    if x >= 0 and x <= 1:
        low = x
        high = 1
    else:
        low = 1
        high = x
    
    epsilon = 0.00000001

    guess = (low + high) / 2

    while abs(guess ** n - x) >= epsilon:
        if guess ** n  > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    
    return guess

def driver():
    # occurrence_count()
    # one_sided_search()
    print(square_root_search(5, 4))

    print(find_nth_root(8, 3))

driver()
