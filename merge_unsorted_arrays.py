#!/usr/bin/env python3

'''
Merging two unsorted arrays in sorted order
Write a SortedMerge() function that takes two lists, each of
which is unsorted, and merges the two together into one new
list which is in sorted (increasing) order. SortedMerge()
should return the new list.

Example:
Input : a[] = {10, 5, 15}
        b[] = {20, 3, 2}
Output : Merge List :
        {2, 3, 5, 10, 15, 20}

Input : a[] = {1, 10, 5, 15}
        b[] = {20, 0, 2}
Output : Merge List :
        {0, 1, 2, 5, 10, 15, 20}
'''


def SortedMerge_1(n, m):
    '''
        Append all the array elements in one storage,
        and then sort the new array
        O(n): O((m+n)log(n + m))
        Space: O(n + m)
    '''
    aux_array = []
    for i in n:
        aux_array.append(i)
    for j in m:
        aux_array.append(j)
    return sorted(aux_array)


def SortedMerge_2(n, m):
    '''
        Sort the individual array elements,
        and then merge into a new array
        O(n): O(nlog(n) + mlog(m) + (n + m))
        Space: O(n + m)
    '''
    # sort list - n
    n.sort()

    # sort list - m
    m.sort()

    aux_array = [0] * (len(n) + len(m))
    i, j, k = 0, 0, 0

    while (i < len(n) and j < len(m)):
        if n[i] <= m[j]:
            aux_array[k] = n[i]
            i += 1
            k += 1
        else:
            aux_array[k] = m[j]
            j += 1
            k += 1
    while i < len(n):
        aux_array[k] = n[i]
        i += 1
        k += 1

    while j < len(m):
        aux_array[k] = m[j]
        j += 1
        k += 1
    return aux_array


if __name__ == '__main__':
    print(SortedMerge_1([10, 5, 15, 3], [20, 3, 2]))
    print(SortedMerge_2([10, 5, 15], [20, 3, 2, 1]))
