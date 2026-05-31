class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        sPass = {}
        res = []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        print(freq)
        for key, val in freq.items():
            sPass[(val,key)] = key
        
        for i in range(k):
            key = max(sPass)
            res.append(sPass[key])
            del sPass[key]
            
        return res

        