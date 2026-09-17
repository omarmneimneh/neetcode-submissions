class TimeMap:

    def __init__(self):
        self.hm = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        res,val = "", self.hm.get(key,[])

        l, r = 0, len(val)-1

        while l <= r:
            mid = (l+r) // 2
            if val[mid][1] > timestamp:
                r = mid-1
            else:
                res = val[mid][0]
                l = mid+1

        return res
        
