class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force:
        Nested for loop where we check the sum of the outer loop integer with the inner loop integer,
        we also need to check that when we are summing these two values they do not share the same index
        number
        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Optimal:
        We can use a hashmap loop through the array and check if this current number is in the map
        if so return this map[this value] and the index number we are on else store the diffence of 
        the current number and the target as the key with the value being the index number.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        pairs = {}

        for i in range(len(nums)):
            if nums[i] in pairs:
                return [pairs[nums[i]], i]
            pairs[target - nums[i]] = i
        