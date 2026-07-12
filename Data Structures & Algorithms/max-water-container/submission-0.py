class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            length = 0
            if heights[left] > heights[right]:
                length = right - left
                res = max(res, heights[right] * length)
                right -= 1
            else:
                length = right - left
                res = max(res, heights[left] * length)
                left += 1
        return res    



        