class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute Force: Nest loop starting from the outer loop create a results string that 
        will have the outer loop starting character and in the inner loop continue to add character 
        into this string until a duplicate occurs. Repeat this and check if the newly made sub string is
        bigger than the current substring result.
        Time Complexity: O(n^2)
        Space Complexity: O(n)

        Optimized:
        Sliding window appraoch, create to pointer one pointer to stay at the starting point the other
        pointer will be the seeker. Add the character from the seeker pointer into a results varaible
        if any character the seeker come across that is already in the result string move the starting pointer
        to that spot. Every time the starting poiint move see if the new generated substring is larger
        than the current in so change the substring.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        start = 0
        seeker = 0
        longest = {}
        result = 0
        while start < len(s) and seeker < len(s):
            longest[s[seeker]] = longest.get(s[seeker], 0) + 1
            while longest[s[seeker]] > 1:
                longest[s[start]] -= 1
                start += 1
            result = max(result, seeker - start + 1)
            seeker += 1
        return result