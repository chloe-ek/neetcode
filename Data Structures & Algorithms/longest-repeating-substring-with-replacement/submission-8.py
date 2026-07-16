class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = defaultdict(int)

        left = 0 
        max_freq = 0 
        longest = 0
        
        for right in range(len(s)):
            right_char = s[right]

            count_dict[right_char] += 1 

            max_freq = max(max_freq, count_dict[right_char])

            if (right - left + 1) - max_freq > k:
                count_dict[s[left]] -= 1
                left += 1 

            longest = max(longest, right - left + 1)

        return longest

                


            