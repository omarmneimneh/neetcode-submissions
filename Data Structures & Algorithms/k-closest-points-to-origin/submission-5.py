class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            distance = -(x**2 + y**2)
            if len(heap) < k:
                heapq.heappush(heap, (distance, (x,y)))
            elif len(heap) == k and distance > heap[0][0]:
                heapq.heappushpop(heap, (distance, (x,y)))
            else:
                continue
        
        res = [x for _,x in heap]
        return res
        
        
