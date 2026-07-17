class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        
        while left < right:
            two_sum = numbers[left] + numbers[right]

            if target == two_sum:
                return [left + 1, right + 1]

            elif target > two_sum:
                left += 1
            
            else:
                right -= 1
        
        return []