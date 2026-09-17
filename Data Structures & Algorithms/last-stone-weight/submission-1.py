class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            if x != y:
                left = max(x,y) - min(x,y)
                heapq.heappush(stones, -left)
        
        if not stones:
            return 0
        return -heapq.heappop(stones)