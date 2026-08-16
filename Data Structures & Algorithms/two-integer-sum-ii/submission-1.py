class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Brute Force:
        Nested loop where the outer loop it summed to every other number in the array excluding itself
        in the inner loop, once the target is reached return the number that summed to the target.
        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Optimized:
        Two pointer approach, if the sum of the left and right pointer is greater than the target
        decrement the right pointer. If less than target increment the left pointer. If the target
        is hit return the left and right pointers.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] <  target:
                left += 1
            else:
                return [left + 1, right + 1]

        