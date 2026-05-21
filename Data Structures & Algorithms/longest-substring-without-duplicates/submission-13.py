class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in seen and seen[char] >= left:
                left = seen[char] + 1
                

            seen[char] = right

            max_len = max(right - left + 1, max_len)

        return max_len


    

        