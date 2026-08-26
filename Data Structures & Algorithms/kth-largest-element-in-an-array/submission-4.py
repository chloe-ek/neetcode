class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [] 

        # nums = [2,3,1,5,4]
        for num in nums:
            heapq.heappush(heap, num)  # heap = [1, 3, 2, 5, 4]

        
        for i in range(len(nums) - k):

            heapq.heappop(heap)

        
        return heap[0]



        