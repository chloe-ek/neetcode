class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        # stones = [2,3,6,2,4]
        for stone in stones:
            heapq.heappush(heap, -stone) # heap = [-6, -4, -3, -2, -2]      
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue

            else:
                new_val = abs(x - y)
                heapq.heappush(heap, -new_val)
            

        return -heap[0] if heap else 0


        
        