#!/usr/bin/env python3


class HashTable(object):
    def __init__(self, length=10):
        self.__array = [None] * length

    def hash(self, key):
        return hash(key) % len(self.__array)

    def add(self, key, value):
        index = self.hash(key)

        if self.__array[index] is not None:
            for kvp in self.__array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    return
            self.__array[index].append([key, value])
        else:
            self.__array[index] = []
            self.__array[index].append([key, value])

    def get(self, key):
        index = self.hash(key)

        if self.__array[index] is None:
            raise KeyError()

        for kvp in self.__array[index]:
            if kvp[0] == key:
                return kvp[1]

        raise KeyError()

    def __repr__(self):
        result = []
        for kvp in self.__array:
            if kvp is not None:
                if len(kvp) > 1:
                    for val in kvp:
                        result.append(f'{val[0]}:{val[1]}')
                else:
                    result.append(f'{kvp[0][0]}:{kvp[0][1]}')
        return ' '.join(result)


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.add('one', 1)
    hash_table.add('two', 2)
    hash_table.add('three', 3)

    print('Hash Table contents:', hash_table)

    print('Index of three:', hash_table.get('three'))

    try:
        print(hash_table.get(-1))
    except Exception as ex:
        print(ex)
