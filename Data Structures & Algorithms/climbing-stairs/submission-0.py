class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev, curr = 1, 2

        # f(n) = f(n-1) + f(n-2)

        for i in range(3, n+ 1):
            new_value = prev + curr
            prev = curr
            curr = new_value

        return curr

        

        

        
        