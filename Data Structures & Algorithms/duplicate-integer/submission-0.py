class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        s = set()
        for nr in nums:
            if nr in s:
                return True
            else:
                s.add(nr)
        return False