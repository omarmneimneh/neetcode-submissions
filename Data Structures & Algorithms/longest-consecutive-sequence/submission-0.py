class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n-1 in nums:
                continue

            x = n
            i = 1

            while x+1 in nums:
                x+=1
                i+=1
            res = max(res, i)

        return res
