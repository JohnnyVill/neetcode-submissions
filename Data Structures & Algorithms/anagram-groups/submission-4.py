class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for i in strs:
            index_key = [0 for i in range(26)]
            for j in i:
                ind = ord(j) - ord('a')
                index_key[ind] += 1
            group[tuple(index_key)].append(i)
        res = []
        for val in group.values():
            res.append(val)
        return res