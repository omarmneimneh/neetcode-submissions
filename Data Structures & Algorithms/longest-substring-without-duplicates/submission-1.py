class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0
        l = r = 0
        while r < len(s):
            if s[r] in seen:
                 while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])                
            r+=1
            maxLen = max(maxLen, (r-l))
        return maxLen