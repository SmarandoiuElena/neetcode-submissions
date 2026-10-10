class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nr = {0:0, 1:0, 2:0}

        for n in nums:
            nr[n] += 1
            
        n = 0
        i = 0
        while (i < len(nums)):
            if nr[n] != 0:
                nums[i] = n
                nr[n] -= 1
                i += 1
            else:
                n += 1
