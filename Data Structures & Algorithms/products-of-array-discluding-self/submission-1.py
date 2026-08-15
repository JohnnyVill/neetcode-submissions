class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Brute Force:
        Createa results array
        Perform a nested loop the outer loop will tell which number to exclude in the inner loop
        then append the product created in the inner loop to the results array
        Time Complexity: O(n^2)
        Space Complexity: O(n)

        Optimal:
        prefix and postfix accumulator
        """
        results = [1 for i in range(len(nums))]
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            results[i] *= prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            results[i] *= postfix
            postfix *= nums[i]
        return results
    
