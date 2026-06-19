class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']': '['}

        for char in s:
            # closed bracket 
            if char in pairs:
                top = stack.pop() if stack else '#'

                if pairs[char] != top:
                    return False

            
            # opened bracket
            else:
                stack.append(char)

        return len(stack) == 0
