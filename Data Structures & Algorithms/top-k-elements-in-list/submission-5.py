class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Brute Force:
        Nested loop that count the max occurences of a number add that number to an results
        array then runs this loop again k amount of time but each time make sure the max 
        number is not already in the results.
        Time Complexity: O(n^2 * k)
        Space Complexity: (k)

        Optimal:
        We are going to use buckets and a hash map. The hash map will store the number
        as a key and the value as the frequency. The in the bucket sort we will use the frequencies to
        know where to index into in the array and put in the number at that index. Once that is
        done we do a reverse loop and return k numbers from the bucket sort that do not equal 0.
        Time Complexity: O(n)
        Space Complexity: O(n + k)

        """
        frequencies = {}

        for i in nums:
            if i not in frequencies:
                frequencies[i] = 0
            else:
                frequencies[i] += 1 
        buckets = [[] for i in range(len(nums))]
        for number, frequency in frequencies.items():
            buckets[frequency].append(number)
            res = []
        for i in range(len(buckets) - 1, -1, -1):
            subarray = buckets[i]
            if subarray:
                res.extend(subarray)
            if len(res) == k:
                return res


        