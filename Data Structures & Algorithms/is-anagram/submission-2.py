class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        frequency = {}

        for i in range(len(s)):
            frequency[s[i]] = frequency.get(s[i], 0) + 1
            frequency[t[i]] = frequency.get(t[i], 0) - 1
        
        for i in frequency.values():
            if i != 0:
                return False
        return True
        