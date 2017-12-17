from collections import defaultdict
from itertools import combinations

class point2d(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'x:%d y:%d' % (self.x, self.y)

quadrants = {}
def initialize():
    quadrants.setdefault('First', [])
    quadrants.setdefault('Second', [])
    quadrants.setdefault('Third', [])
    quadrants.setdefault('Fourth', [])

def checkquadrants(point):
    if point.x >= 0 and point.y >= 0:
        quadrants['First'].append((point.x, point.y))
    elif point.x < 0 and point.y >= 0:
        quadrants['Second'].append((point.x, point.y))
    elif point.x < 0 and point.y < 0:
        quadrants['Third'].append((point.x, point.y))
    else:
        quadrants['Fourth'].append((point.x, point.y))

def arecolinear(points, q):
    xdiff1 = float(points[1][0] - points[0][0])
    ydiff1 = float(points[1][1] - points[0][1])
    xdiff2 = float(points[2][0] - points[1][0])
    ydiff2 = float(points[2][1] - points[1][1])

    if points[0] in q:
        q.remove(points[0])
    if points[1] in q:
        q.remove(points[1])
    if points[2] in q:
        q.remove(points[2])
    # infinite slope?
    if xdiff1 == 0 or xdiff2 == 0:
        return xdiff1 == xdiff2
    elif float(ydiff1/xdiff1) == float(ydiff2/xdiff2):
        return True
    else:
        return False

def main():
    initialize()
    points = []
    points.append(point2d(1, 2))
    points.append(point2d(-1, -2))
    points.append(point2d(2, 4))
    points.append(point2d(3, 6))
    points.append(point2d(-3, 2))
    points.append(point2d(2, -2))
    points.append(point2d(1, 5))
    for p in points:
        checkquadrants(p)
    count = 0
    #First Quad
    fq = quadrants.get('First')
    if len(fq) == 1:
        count += 1
    elif len(fq) == 2:
        count += 1
    elif len(fq) > 2:
        fqcomb = combinations(fq, 3)
        for comb in fqcomb:
            if len(comb) == 1:
                count += 1
            elif arecolinear(comb, fq):
                count += 1
            else:
                count += 2
            fqcomb = combinations(fq, 3)

    #Second Quad
    # sq = quadrants.get('Second')
    # if len(sq) == 1:
    #     count += 1
    # elif len(sq) == 2:
    #     count += 1
    # elif len(sq) > 2:
    #     for comb in combinations(sq, 3):
    #         if len(comb) == 1:
    #             count += 1
    #         elif arecolinear(comb, sq):
    #             count += 1
    #         else:
    #             count += 2

    # #Third Quad
    # tq = quadrants.get('Third')
    # if len(tq) == 1:
    #     count += 1
    # elif len(tq) == 2:
    #     count += 1
    # elif len(tq) > 2:
    #     for comb in combinations(tq, 3):
    #         if len(comb) == 1:
    #             count += 1
    #         elif arecolinear(comb, tq):
    #             count += 1
    #         else:
    #             count += 2
    # #Fourth Quad
    # lq = quadrants.get('Third')
    # if len(lq) == 1:
    #     count += 1
    # elif len(lq) == 2:
    #     count += 1
    # elif len(lq) > 2:
    #     for comb in combinations(lq, 3):
    #         if len(comb) == 1:
    #             count += 1
    #         elif arecolinear(comb, lq):
    #             count += 1
    #         else:
    #             count += 2
    print(count)

main()
