class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s):
        res =[]
        i = 0

        while i < len(s):
            j = i
            # find the '#' 
            while s[j] != '#':
                j += 1
            
            # extract the word's length
            length = int(s[i:j])

            # get actual word
            words = s[j + 1: j + 1 + length]
            res.append(words)

            i = j + 1 + length

        return res



            

        



