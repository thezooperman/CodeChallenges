# code
'''
Given a array of N strings, find the longest common
prefix among all strings present in the array.

Input:
The first line of the input contains an integer T which
denotes the number of test cases to follow. Each test case
contains an integer N. Next line has space separated N strings.

Output:
Print the longest common prefix as a string in the given array.
If no such prefix exists print "-1"(without quotes).

e.g.:
    Input:
        2
        4
        geeksforgeeks geeks geek geezer
        3
        apple ape april

    Output:
        gee
        ap
'''


def lcp(string_arr, n):
    '''
        Runtime: O(nlog(n))
        Because of the sort operation
    '''
    return_val = ''
    if not string_arr:
        print(-1)
        return
    string_arr.sort()
    leftmost_el = string_arr[0]
    rightmost_el = string_arr[-1]

    min_len = min(len(leftmost_el), len(rightmost_el))

    for i in range(min_len):
        if leftmost_el[i] == rightmost_el[i]:
            return_val += rightmost_el[i]
        else:
            break
    if not return_val:
        print(-1)
    else:
        print(return_val)
    return


if __name__ == '__main__':
    t = int(input().strip())
    for tc in range(t):
        n = int(input().strip())
        string_arr = input().strip().split(None)
        lcp(string_arr, n)
