def is_sorted(array: list, n: int) -> bool:
    if not array or not n:
        raise TypeError('Bad shit!, pass proper values')
    if n == 1:
        return True
    return False if array[n - 1] < array[n - 2] else is_sorted(array, n-1)

if __name__ == '__main__':
    array = [1,2,3,4,5]
    print(f'Is array: {array} sorted: {is_sorted(array, len(array))}')
    array = [1,2, 4, 3, 5]
    print(f'Is array: {array} sorted: {is_sorted(array, len(array))}')

