class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        min_frequency = 0
        max_frequnecy = 0
        result = []
        hashtable = {}

        for i in range(len(nums)):

            if nums[i] in hashtable:
                hashtable[nums[i]] += 1
            else:
                hashtable[nums[i]] = 1

            if hashtable[nums[i]] > max_frequnecy:
                max_frequnecy = hashtable[nums[i]]

        while (k):
            for i, j in hashtable.items():
                if j == max_frequnecy and k != 0:
                    result.append(i)
                    k -= 1
                if k == 0:
                    break
            max_frequnecy -= 1
        return result
        
