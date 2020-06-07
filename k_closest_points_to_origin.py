"""
K Closest Points to Origin

We have a list of points on the plane.  Find the K closest
points to the origin (0, 0).

(Here, the distance between two points on a plane is the
Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed
to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]

Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is
just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""


import math
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]

    def kClosest_old(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return [[]]

        heap_data = []
        distance_data = defaultdict(list)

        for point in points:
            distance = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))
            heapq.heappush(heap_data, distance)
            if point not in distance_data[distance]:
                distance_data[distance].append(point)

        # print(heap_data)
        # print(distance_data)

        return_val = []
        for k_th in range(K):
            distance = heapq.heappop(heap_data)
            data = distance_data[distance]

            if len(data) > 1:
                if data[0] not in return_val or data[1] not in return_val:
                    return_val.extend(data)
            else:
                if data not in return_val:
                    return_val.append(*data)

        return return_val


if __name__ == "__main__":
    obj = Solution()

    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    output = [[-2, 2]]

    actual = obj.kClosest(points, K).sort()

    assert actual == output.sort()

    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    output = [[3, 3], [-2, 4]]

    actual = obj.kClosest(points, K).sort()

    assert actual == output.sort()
