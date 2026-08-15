class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Brute Force:
        Create a results array.
        create a map of the sorted string and the value it actually is.
        sort all the string in the array. Insert the first string into a subarry of the result array.
        If the next string is the same are the string in the subarray add it into that subarrary. Else
        create a new sub array with this new string repeat this process. The loop through this result array
        and replace the string with the value if the map
        Time Complexity: O(n * nlogn)
        Space Complexity: O(2n)
        """
        """
        Optimal:
        Create result array
        Create a Hash Map: this hash map will store a key value of length 26 which will hold the 
        pattern the string makes when each character is substracted from the ascii value of 'a'. This
        will show if the string are anagrams since it only check the frequency of character the string
        contains.
        Time Complexity: O(n * m) n is the length of the array and m is the length of the string
        Space Complexity: (2n)
        """
        results = []
        sublist_map = defaultdict(list)

        for word in strs:
            sequence = [0 for i in range(26)]
            for c in word:
                index = ord(c) - ord('a')
                sequence[index] += 1
            sublist_map[tuple(sequence)].append(word)
        
        for val in sublist_map.values():
            results.append(val)
        return results