class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l <= r:
            k = 0
            mid = (l+r)//2
            for pile in piles:
                k+= math.ceil(pile/mid)
            
            if k > h:
                l = mid+1
            else:
                r = mid-1

        return l
