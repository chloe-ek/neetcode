class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_capacity = 0
        left, right = 0, len(heights) - 1

        while left < right:
            capacity = min(heights[left], heights[right]) * (right - left)

            max_capacity = max(capacity, max_capacity)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        
        return max_capacity