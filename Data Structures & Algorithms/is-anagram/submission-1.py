class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ana = {}

        for i in range(len(s)):
            ana[s[i]] = 1 + ana.get(s[i], 0)
            ana[t[i]] = -1 + ana.get(t[i], 0)
        
        if max(ana.values()) != 0:
            return False
        else:
            print(max(ana.values()))
            return True
        