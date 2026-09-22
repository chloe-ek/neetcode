class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 

        for i in range(1, n + 1):

            # last digit alone decode 
            one_digit = s[i-1]

            if one_digit != '0':
                dp[i] += dp[i-1]

            # two last digits decode 
            if i >= 2:
                two_digit_str = s[i-2:i]
                two_digit_num = int(two_digit_str)

                if two_digit_num >= 10 and two_digit_num <= 26:
                    dp[i] += dp[i-2]

        return dp[n]

