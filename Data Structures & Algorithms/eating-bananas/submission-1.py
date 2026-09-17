class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l ,r = 1, max(piles)
        k = r

        while l <= r:
            mid = (r+l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours > h:
                l = mid+1
            else:
                k = mid
                r = mid-1 
        return k