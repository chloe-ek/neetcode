class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [] 

        # nums = [2,3,1,5,4]
        for num in nums:
            heapq.heappush(heap, num)  # heap = [1, 2, 3, 4, 5]

        
        for i in range(len(nums) - k):

            heapq.heappop(heap)

        
        return heap[0]



        