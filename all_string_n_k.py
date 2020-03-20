def all_strings(array, n, k):
    if n < 1:
        print(*array)
    else:
        for i in range(k):
            array[n - 1] = i
            all_strings(array, n - 1, k)

if __name__ == '__main__':
    n, k = 2, 3
    array = [0] * n
    all_strings(array, n, k)

