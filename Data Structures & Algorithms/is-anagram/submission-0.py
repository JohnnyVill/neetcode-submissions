class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            freq[t[i]] = -1 + freq.get(t[i], 0)
        
        for val in freq.values():
            if val != 0:
                return False
        return True
