class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # 1. max banana is the max in piles 
        # 2. len(piles) is minimum hours len(piles) <= h
        # 3. in the range 1 <= rate <= max(piles)
        # 4. search the feasible rate
        # 5. calculates the total hour 

        #  piles = [1,4,3,2], h = 9


        def calcuates_time(rate, piles, h):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / rate)
            return (total_hours <= h)

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if calcuates_time(mid, piles, h):
                right = mid
            else:
                left = mid + 1

        return left






