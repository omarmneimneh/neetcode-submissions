class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        curr = [intervals[0][0],intervals[0][1]]
        for start,end in intervals:
            if start <= curr[1]:
                curr = [curr[0], max(curr[1], end)]
            else:
                res.append(curr)
                curr = [start, end]
        res.append(curr)
        return res