class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}

        for i in nums:
            if i in duplicates:
                return True
            else:
                duplicates[i] = 1 + duplicates.get(i,0)
        return False
        