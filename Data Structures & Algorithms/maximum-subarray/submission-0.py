class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = float("-inf"),0

        for n in nums:
            currSum += n
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum
