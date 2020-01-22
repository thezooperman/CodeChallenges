class Indexed():
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value < other.value
    
    def __str__(self):
        return str.format('Value:{} Index:{}\n', self.value, self.index)


def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    print(swaps)

def minimumSwaps2(arr):
    if not arr:
        raise TypeError('Bad shit!')
    '''
    indexes = [_ for _ in range(1, len(arr) + 1, 1)]

    swaps = 0
    for i, v in enumerate(arr):
        if v != indexes[i]:
            arr[i], arr[indexes[v - 1] - 1] = arr[indexes[v - 1] - 1], arr[i]
            swaps += 1
    return swaps
    '''
    swaps = 0
    l = [0] * len(arr)

    for i, v in enumerate(arr):
        l[i] = Indexed(v, i)
    
    # sort the list by its values
    l.sort()
    print(*l)
    i = 0
    while i < len(l):
        if l[i].index == i:
            i += 1
        else:
            # swap(vec[i].first,vec[vec[i].second].first); 
            #swap(vec[i].second,vec[vec[i].second].second);  
            
            l[i].value, l[l[i].index].value = l[l[i].index].value, l[i].value
            l[i].index, l[l[i].index].index = l[l[i].index].index, l[i].index

            if i != l[i].index:
                i -= 1

            swaps += 1

    print(swaps)



if __name__ == '__main__':
    # minimumSwaps([1,5,4,3,2])
   minimumSwaps([1 ,3 ,5 ,2 ,4 ,6 ,7])
