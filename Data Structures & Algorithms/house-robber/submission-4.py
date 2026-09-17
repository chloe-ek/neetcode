class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]

        for i in range(1, n):
            skip = dp[i - 1]
            rob_i = nums[i] + (dp[i-2] if i >=2 else 0)
            dp[i] = max(skip, rob_i)

        return dp[n-1]
