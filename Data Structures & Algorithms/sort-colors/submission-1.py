class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l0, mid, hi = 0, 0, n - 1

        while (mid <= hi):
            if nums[mid] == 0:
                nums[l0], nums[mid] = nums[mid], nums[l0]
                l0 += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1