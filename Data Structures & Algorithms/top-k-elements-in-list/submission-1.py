class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for n in nums:
            if n in store:
                store[n] += 1
            else:
                store[n] = 1
        
        sorted_elements = sorted(store.keys(), key=lambda x: store[x], reverse=True)

        return sorted_elements[:k]
            
        