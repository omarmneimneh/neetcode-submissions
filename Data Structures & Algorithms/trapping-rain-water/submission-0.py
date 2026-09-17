class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxL, maxR = 0, 0
        l, r = 0, len(height)-1

        while l < r:
            maxL, maxR = max(maxL, height[l]), max(maxR, height[r])
            res+= min(maxL, maxR)-min(height[l], height[r])
            if maxL > maxR:
                r-=1
            else:
                l+=1
        return res