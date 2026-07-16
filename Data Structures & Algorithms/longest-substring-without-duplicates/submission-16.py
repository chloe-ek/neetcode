class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = 0
        length = 0

        for right in range(len(s)):

            char = s[right]

            while char in seen:
                left_char = s[left]
                seen.remove(left_char)
                left += 1

            seen.add(char)
            length = right - left + 1
            longest = max(longest, length)

        return longest
            
                





        