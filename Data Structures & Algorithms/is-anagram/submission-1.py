class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        stored = {}

        for i in s:
            
            stored[i] = stored.get(i, 0) + 1

        for i in t:
            if i not in stored or stored[i] == 0:
                return False
            
            stored[i] -= 1

        return True


