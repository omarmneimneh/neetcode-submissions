class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            if x != y:
                left = max(x,y) - min(x,y)
                heapq.heappush(heap, -left)
        
        if not heap:
            return 0
        return -heapq.heappop(heap)