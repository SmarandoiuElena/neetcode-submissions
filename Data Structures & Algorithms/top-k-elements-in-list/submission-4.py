import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashtable = {}
        result = []
        heap = []
        heapq.heapify(heap)

        for i in range(len(nums)):

            if nums[i] in hashtable:
                hashtable[nums[i]] += 1
            else:
                hashtable[nums[i]] = 1

        for i, j in hashtable.items():
            
            heapq.heappush(heap, [j, i])
            if len(heap) > k:
                heapq.heappop(heap)

        while k:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result
        

            
            
        
        
