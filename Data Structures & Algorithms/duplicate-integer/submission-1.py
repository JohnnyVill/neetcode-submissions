class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        for values in freq.values():
            if values > 1:
                return True
        return False
