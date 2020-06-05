"""
Active and Inactive cells after k Days
Given a binary array of size n where n > 3. A true (or 1) value
in the array means active and false (or 0) means inactive. Given a
number k, the task is to find count of active and inactive cells
after k days. After every day, status of i’th cell becomes active if
left and right cells are not same and inactive if left and right cell
are same (both 0 or both 1).

Since there are no cells before leftmost and after rightmost cells,
the value cells before leftmost and after rightmost cells is always
considered as 0 (or inactive).


Examples:

Input  : cells[] = {1, 0, 1, 1}, k = 2
Output : Active cells = 3, Inactive cells = 1
After 1 day,  cells[] = {0, 0, 1, 1}
After 2 days, cells[] = {0, 1, 1, 1}

Input : cells[] = {0, 1, 0, 1, 0, 1, 0, 1},  k = 3
Output: Active Cells = 2 , Inactive Cells = 6
Explanation : 
After 1 day, cells[] = {1, 0, 0, 0, 0, 0, 0, 0}
After 2 days, cells[] = {0, 1, 0, 0, 0, 0, 0, 0}
After 3 days, cells[] =  {1, 0, 1, 0, 0, 0, 0, 0}

Input : cells[] = {0, 1, 1, 1, 0, 1, 1, 0},  k = 4
Output: Active Cells = 3 , Inactive Cells = 5
"""

from typing import List


def set_cell_value(x: int, arr: List[int], temp_store: List[int]) -> None:
    if 0 <= x < len(arr):
        if x == 0:
            temp_store[x] = 0 ^ arr[x + 1]
        elif x == len(arr) - 1:
            temp_store[x] = 0 ^ arr[x - 1]
        else:
            temp_store[x] = arr[x - 1] ^ arr[x + 1]


def activeAndInactive(cells: List[int], k: int) -> tuple:
    temp_store = list(cells)
    while (k):
        k -= 1
        i = 0
        while i < len(cells):
            set_cell_value(i, cells, temp_store)
            i += 1
        cells, temp_store = temp_store, cells

    active = inactive = 0
    for i in cells:
        if i == 0:
            inactive += 1
        else:
            active += 1

    return (active, inactive)


if __name__ == "__main__":
    cells = [1, 0, 1, 1]
    k = 2

    active, inactive = activeAndInactive(cells, k)
    print("Array", cells)
    print("Acitive:{}, Inactive:{}".format(active, inactive), flush=True) # Active - 3, Inactive = 1


    cells = [0, 1, 0, 1, 0, 1, 0, 1]
    k = 3

    active, inactive = activeAndInactive(cells, k)
    print("Array", cells)
    print("Acitive:{}, Inactive:{}".format(active, inactive), flush=True) # Active - 2, Inactive = 6


    cells = [0, 1, 1, 1, 0, 1, 1, 0]
    k = 4

    active, inactive = activeAndInactive(cells, k)
    print("Array", cells)
    print("Acitive:{}, Inactive:{}".format(active, inactive), flush=True) # Active - 3, Inactive = 5