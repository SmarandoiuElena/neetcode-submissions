class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p, q = 1, 1
        result = []
        zero_numbers = 0
        for n in nums:
            if n != 0:
                q *= n
            else:
                zero_numbers += 1
            p *= n

        if zero_numbers > 1:
            return [0] * len(nums)
            
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(q)
            else:
                result.append(int(p / nums[i]))

        return result
