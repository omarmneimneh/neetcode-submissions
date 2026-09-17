class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                idx = stack.pop()[1]
                res[idx] = i - idx
            stack.append((temp, i))


        while stack:
            idx = stack.pop()[1]
            res[idx] = 0
        
        return res