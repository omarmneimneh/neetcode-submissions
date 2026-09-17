class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for word in strs:
            hm[''.join(sorted(word))].append(word)
        
        return list(hm.values())