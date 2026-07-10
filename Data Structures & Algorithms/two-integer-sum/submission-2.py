class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for ind, val in enumerate(nums):
            if val in pairs:
                return [pairs[val], ind]
            else:
                pairs[target - val] = ind
        