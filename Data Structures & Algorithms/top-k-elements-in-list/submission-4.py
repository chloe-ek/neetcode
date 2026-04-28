import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for n in nums:
            store[n] = store.get(n, 0) + 1
        
        min_heap = []

        for num, freq in store.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = []
        while min_heap:
            freq, num = heapq.heappop(min_heap)
            res.append(num)
            
        return res
        