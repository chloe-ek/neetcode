class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']': '[', ')': '(', '}': '{'}
        stack = []

        for char in s:
            if char in pairs:
                
                elem = stack.pop() if stack else '*'

                if elem != pairs[char]:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0


        