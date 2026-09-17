class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sub in matrix:
            l, r = 0, len(sub)-1
            if sub[l] > target or sub[r] < target:
                continue        
            while l <= r:
                mid = l + (r-l) // 2
                print(sub[mid])
                if sub[mid] == target:
                    return True
                if sub[mid] > target:
                    r = mid-1
                else:
                    l = mid + 1
        return False