from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        res = 0
        q = deque()
        while maxHeap or q:
            res += 1

            if not maxHeap:
                res = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                heapq.heappush(maxHeap, q.popleft()[0])
        return res
        