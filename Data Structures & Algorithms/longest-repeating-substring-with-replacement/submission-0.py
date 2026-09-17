class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        maxC = 0
        l = r = 0
        hm = {}

        while r < len(s):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxC = max(maxC, hm[s[r]])

            if (r - l + 1) - maxC > k:
                hm[s[l]]-=1
                l+=1
            
            r+=1
        return (r-l)