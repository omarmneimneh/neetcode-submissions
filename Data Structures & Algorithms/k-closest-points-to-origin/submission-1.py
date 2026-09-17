from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y = point[1]

            distance = sqrt((x**2) + (y**2))
            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            else:
                if heap[0][0]  < distance:
                    heapq.heappushpop(heap, (-distance, point))
        return [y for (x,y) in heap]