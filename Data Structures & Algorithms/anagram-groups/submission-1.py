class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #loop through each word in the array
        #in this loop create an array of the same length of the alphabet(26) with each value = 0
        #make a inner loop going through each individual letter in the word and subract it from a base
        #make the base the ascii value of 'a' and subract every other letter ascii value from this
        #doing so will make a value from 0-25 which is going to be as an index values in the array we created earlier
        #then add these array with different patteren into a dictionary and return the length of dictionary

        resDict = defaultdict(list)
        res = []
        for word in strs:
            arr = [0]*26
            for c in word:
                ind = ord(c) - ord('a')
                arr[ind] += 1
            resDict[tuple(arr)].append(word)
        for val in resDict.values():
            res.append(val)
        return res