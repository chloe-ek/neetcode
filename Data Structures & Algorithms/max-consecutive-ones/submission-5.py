class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        max_count = 0

        for c in nums:
            if c:
                count += 1
                
            else:
                max_count = max(max_count, count)
                count = 0
            
        return max(max_count, count)
            
        