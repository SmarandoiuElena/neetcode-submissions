class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        start = []
        hashtable = {}
        # insert all numbers in the hashtable in O(n)
        for n in nums:
            hashtable[n] = 1
        
        for n in nums:
            if n - 1 not in hashtable:
                start.append(n)

        for s in start:
            length = 1
            index = 1
            for n in nums:
                if s + index in hashtable:
                    length += 1
                    index += 1
                else:
                    break
            if length > longest:
                longest = length
                
        return longest
