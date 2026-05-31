class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        for key, val in freq.items():
            bucket[val].append(key)
        
        for i in range(len(bucket) -1, -1, -1):
            
            if len(res) == k:
                return res
            if bucket[i] != []:
                res.extend(bucket[i])
