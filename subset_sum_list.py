# subset_sum_list.py
'''
Given an array, find all the possible
subsets, which will match the given sum
arr = [2, 6, 4, 10]
sum = 16
output sets = {10, 6}, {2, 4, 10}
'''

counter = 0


def findSubsetList(arr, n, currSum, sol, index):
    global counter
    counter += 1
    if currSum == n:
        print('Solution Found:', *(arr[i] for i in
              range(len(sol)) if sol[i] == 1))
    elif index == len(arr) or currSum > n:
        return
    else:
        sol[index] = 1
        currSum += arr[index]
        findSubsetList(arr, n, currSum, sol, index + 1)
        currSum -= arr[index]
        sol[index] = 0
        findSubsetList(arr, n, currSum, sol, index + 1)


def main(arr, n):
    findSubsetList(arr, n, 0, [0] * len(arr), 0)


main([2, 6, 4, 10], 16)
print('Number of iterations:', counter)
