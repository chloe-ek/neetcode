class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0 


        def expand(left, right):
            substring = 0

            while left >= 0 and right < len(s) and s[right] == s[left]:
                substring += 1
                left -= 1
                right += 1

            return substring 

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            count += odd
            count += even
            
            
        return count


        