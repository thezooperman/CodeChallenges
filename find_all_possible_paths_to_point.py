# find_all_possible_paths_to_point.py


def calculatePath(row, col, i, j, path):
    '''
        Accumulate all possible paths from
        point A to point B, in a matrix
        :type row: int
        :type col: int
        :type i: int
        :type j: int
        :type path : string
    '''
    if i == row - 1 and j == col - 1:
        # print(path)
        global paths
        paths.append(path)
        return
    # Vertical Downard movement
    # Trace back if solution is not reached
    if i == row - 1:
        calculatePath(row, col, i, j + 1, path + 'V')
        return
    # Horizontal Rightward movement
    # Trace back is solution is not reached
    if j == col - 1:
        calculatePath(row, col, i + 1, j, path + 'H')
        return

    calculatePath(row, col, i + 1, j, path + 'H')
    calculatePath(row, col, i, j + 1, path + 'V')


def countPath(x, y, i, j):
    '''Count the path occurence for all possible combinations
        from 0,0 to x,y
      :type x: int
      :type y: int
      :type i: int
      :type j: int
      :rtype: int
    '''
    if i < x and j < y:
        if i == x - 1 and j == y - 1:
            return 1
        return countPath(x, y, i + 1, j) +\
            countPath(x, y, i, j + 1)

    return 0


paths = []


def getSafePaths(journeys):
    if journeys is None:
        return None
    for j in journeys:
        x, y, k = map(int, j.split())
        # print(countPath(x + 1, y + 1, 0, 0))
        calculatePath(x + 1, y + 1, 0, 0, '')
        paths.sort()
        print(paths[k])
        paths.clear()


getSafePaths(['2 2 2'])
getSafePaths(['2 2 3'])
getSafePaths(['2 3 3'])
