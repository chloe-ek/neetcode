class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = [] # new list 

        for char in s: 
            if char.isalnum(): # if they are alpha or num
                cleaned.append(char.lower()) # add lowercase in the basket
                
        # list comprehension
        # cleaned = "".join([char.lower() for char in s if char.isalnum()])

        return cleaned == cleaned[::-1]




        