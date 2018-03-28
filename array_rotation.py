# array_rotation.py
'''
Implement an array left rotation with
O(1) space
'''


def array_rotation(array, rotate_by):
    length = len(array) - 1
    for i in range(rotate_by):
        temp = array[0]
        for j in range(length):
            array[j] = array[j + 1]
        array[length] = temp
    return array


def array_right_rotate(array, rotate_by):
    length = len(array) - 1
    for i in range(rotate_by):
        temp = array[length]
        for j in range(length, 0, -1):
            array[j] = array[j - 1]
        array[0] = temp
    return array


print(array_rotation([1, 2, 3, 4, 5, 6, 7], 2))
print(array_right_rotate([1, 2, 3, 4, 5, 6, 7], 2))
