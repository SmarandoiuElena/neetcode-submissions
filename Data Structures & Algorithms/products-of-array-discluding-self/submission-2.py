class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []
        result = []
        p = 1
        for i in range(len(nums)):
            suffix.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix.append(p)
            p *= nums[i]
        prefix = prefix[::-1]

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
            
        return result
        