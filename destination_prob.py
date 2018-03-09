#  destination_prob.py


'''
Given coordinates of a source point (x1, y1) determine if it is possible to
reach the destination point (x2, y2). From any point (x, y) there only two
types of valid movements:
(x, x + y) and (x + y, y).
Return a boolean true if it is possible else return false.
Note: All coordinates are positive.
'''


def find_dest(sx, sy, dx, dy):
    '''Find if destination can be reached
       @sx: x1
       @sy: y1
       @dx: x2
       @dy: y2 
    '''
    if sx > dx or sy > dy:
        return False
    if sx == dx and sy == dy:
        return True
    return find_dest(sx + sy, sy, dx, dy) or find_dest(sx, sx + sy, dx, dy)


print('Is Destination Reachable for X->(2, 10) and Y->(26, 12): ' +
      str(find_dest(2, 10, 26, 12)))
print('Is Destination Reachable for X->(20, 10) and Y->(6, 12): ' +
      str(find_dest(20, 10, 6, 12)))
