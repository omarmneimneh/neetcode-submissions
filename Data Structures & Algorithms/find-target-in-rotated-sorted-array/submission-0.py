class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            #rotated check
            if nums[l] <= nums[mid]:
                if target > nums[mid] or nums[l] > target:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid-1
                else:
                    l = mid+1
        return -1