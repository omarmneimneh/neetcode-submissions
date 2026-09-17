class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            res = 0
            while num:
                res += (num%10) ** 2
                num = num // 10
            return res
        
        slow, fast = n, square(n)

        while slow != fast:
            fast = square(square(fast))
            slow = square(slow)
        return slow == 1