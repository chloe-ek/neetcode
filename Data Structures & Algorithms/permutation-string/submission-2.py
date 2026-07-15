class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # ex. {a : 1, b: 1, c:1 }
        store = defaultdict(int)
        for s in s1:
            store[s] += 1

        left = 0 
        window = defaultdict(int)

        # using window algorithm
        for right in range(len(s2)):
            char_right = s2[right]
            window[char_right] += 1
            
            # shrink windown if the length is bigger than s1 
            if (right - left + 1) > len(s1):
                char_left = s2[left]
                window[char_left] -= 1
                # delete left character completely first
                if window[char_left] == 0:
                    del window[char_left]
                left += 1

            if store == window:
                return True 

        return False

        




        