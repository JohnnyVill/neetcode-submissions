class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        max_frequency = 0
        result = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1

            max_frequency = max(
                max_frequency,
                counts[s[right]]
            )

            # while number of replacements needed > k:
            # get window length - max frequency to find how many non matching character are inside
            while (right - left + 1) - max_frequency > k:
                counts[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result