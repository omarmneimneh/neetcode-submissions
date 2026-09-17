class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = defaultdict(str)

        for c in s:
            hm[c]= hm.get(c, 0) + 1
        
        for c in t:
            if c not in hm or hm[c] == 0:
                return False
            hm[c]-=1
        print(hm)
        for x,y in hm.items():
            if y > 0: return False
        return True
