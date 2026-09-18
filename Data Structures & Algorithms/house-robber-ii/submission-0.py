class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_linear(arr):
            m = len(arr)
            dp = m * [0]

            dp[0] = arr[0]

            for i in range(1, m):
                prev = dp[i-1]
                curr = arr[i] + (dp[i-2] if i >= 2 else 0)
                dp[i] = max(prev, curr)

            return dp[m-1]

        # first house to the second last house
        from_first = rob_linear(nums[0:n-1])
        # second house to the last house
        from_second = rob_linear(nums[1:n])

        return max(from_first, from_second)

