class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
            Brute Force:
            Nested loop where the outer loop is the current number we want to 
            check if there is a duplicate and the inner loop compares that number
            to the rest of the digits in the array
            Time Complexity: O(n^2)
            Space Complexity: O(n)

            Optimal:
            Create a hash map, loop through array and add every number into the hashmap
            if that number is already in the hash map return true since that means there
            is a duplicate
            Time Complexity: O(n)
            Space Complexity: O(n + m)
        """
        frequency = {}

        for i in nums:
            if i  not in frequency:
                frequency[i] = 0
            else:
                return True
        return False