class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        seq = set(nums)
        curr = 0
        res = 0
        
        for i in seq:
            if i - 1 not in seq:
                j = i
                while j in seq:
                    j += 1
                    curr += 1
            res = max(res, curr)
            curr = 0
            
        res = max(res,curr)
        return res        
            



        