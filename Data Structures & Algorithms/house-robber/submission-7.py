class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = n * [0] # save the max amount of money so far

        dp[0] = nums[0]

        for i in range(1, n):
            prev = dp[i-1]
            curr = nums[i] + (dp[i-2] if i >= 2 else 0)
            dp[i] = max(prev, curr)

        return dp[n-1]

