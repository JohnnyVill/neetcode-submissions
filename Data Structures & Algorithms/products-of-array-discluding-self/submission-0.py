class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        res = []
        for i in range(len(nums) -1):
            if not arr1:
                arr1.append(nums[i])
            else:
                prod = arr1[-1] * nums[i]
                arr1.append(prod)
        
        for i in range(len(nums)-1, 0, -1):
            if not arr2:
                arr2.append(nums[i])
            else:
                prod = arr2[-1] * nums[i]
                arr2.append(prod)
        res.append(arr2[-1])
        j = 0
        for i in range(len(arr2) - 2, -1, -1):
            prod = arr2[i] * arr1[j]
            res.append(prod)
            j += 1
        res.append(arr1[-1])
        return res
            

