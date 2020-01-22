def left_rotate(arr, n, k)-> None:
    '''
        Rotate an array left, by k elements
        Args:
            arr, int[]: array of integers
            n, int: length of array arr
            k, int: rotate value
    '''
    if not arr or not n:
        raise TypeError('WTF!!')

    for i in range(n):
        print(arr[(i + k) % n], end=' ')

    print(flush=True)

def right_rotate(arr, n, k)-> None:
    '''
        Rotate an array right, by k elements
        Args:
            arr, int[]: array of integers
            n, int: length of array arr
            k, int: rotate value
    '''
    if not arr or not n:
        raise TypeError('WTF!!')

    for i in range(n):
        print(arr[((i - k) % n + n)% n], end=' ')

    print(flush=True)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(f'Original array: {arr}')
    l = len(arr)
    k = 2
    print('Left Rotate:')
    left_rotate(arr, l, k)
    print('Right Rotate:')
    right_rotate(arr, l, k)

