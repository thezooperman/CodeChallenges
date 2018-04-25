# dp_total_ways_to_form_n_sum.py

'''
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N'
using the sum of the given three numbers.
(allowing repetitions and different arrangements).
Total number of ways to form 6 is : 8
1+1+1+1+1+1
1+1+1+3
1+1+3+1
1+3+1+1
3+1+1+1
3+3
1+5
5+1
'''


def non_dynamic_solution(nums, n):
    '''Given the keys - DP[n] = DP[n - 1] + DP[n-3] + DP[n-5]'''
    if n < 0:
        return 0
    if n == 0:
        return 1
    return non_dynamic_solution(nums, n - 1) +\
        non_dynamic_solution(nums, n - 3) + \
        non_dynamic_solution(nums, n - 5)


def dynamic_solution(nums, n, DP):
    '''Given the keys - DP[n] = DP[n - 1] + DP[n-3] + DP[n-5]
       Uses Memoization
    '''
    if n < 0:
        return 0
    if n == 0:
        return 1
    if DP[n - 1] != -1:
        return DP[n - 1]
    DP[n - 1] = dynamic_solution(nums, n - 1, DP) +\
        dynamic_solution(nums, n - 3, DP)\
        + dynamic_solution(nums, n - 5, DP)
    return DP[n - 1]


def main():
    n = 6
    print('Non - DP-->Number of ways to form %s from %s: %s' %
          (n, [1, 3, 5], non_dynamic_solution([1, 3, 5], n)))
    n = 40
    DP = [-1] * n
    print('DP-->Number of ways to form %s from %s: %s' %
          (n, [1, 3, 5], dynamic_solution([1, 3, 5], n, DP)))


if __name__ == '__main__':
    main()
