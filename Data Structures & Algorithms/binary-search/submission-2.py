class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Brute Force: Loop through the list untill you find the target, then return the 
        ith position of that number.
        Time Complexity: O(n)
        Space Complexity: O(1)

        Optimized: Since the list is already in order, we can use a binary search. By making 
        three pointers, a left pointer, middle pointer and right pointer. If the middle pointer
        is < target, make the left pointer = middle + 1 else if the middle pointer value is > target
        right = middle + 1 continue this until the target is found.
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1