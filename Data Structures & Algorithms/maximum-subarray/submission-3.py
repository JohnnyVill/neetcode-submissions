class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = None
        max_sub = None
        for acc in range(len(nums)):
            if sub == None:
                sub = nums[acc]
                max_sub = nums[acc]
            elif sub < 0 and nums[acc] >= 0:
                sub = nums[acc]
                max_sub = max(sub, max_sub)

            elif sub < 0 and nums[acc] < 0:
                sub = max(sub, nums[acc])
                max_sub = max(sub, max_sub)

            else:
                sub += nums[acc]
                max_sub = max(sub, max_sub)
        return max_sub
            
            
