class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        stored = {}
        
        for i, num in enumerate(nums):
            complement = target - num

            if complement in stored:
                return [stored[complement], i]

            stored[num] = i
        
        return []

