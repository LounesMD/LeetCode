class Solution:
    def numDecodings(self, s: str) -> int:
        # Step 1: Recursion
        # Step 2: Memoization
        memo = [-1] * (len(s) + 1)
        poss_values1 = [str(i) for i in range(1, 10)] # All possible values [1,9]
        poss_values2 = [str(i) for i in range(10, 27)] # All possible values [10,26]

        def dp_fn(idx):
            if idx == len(s):
                return 1

            if s[idx] == "0":
                return 0

            if memo[idx] != -1:
                return memo[idx]

            r = dp_fn(idx+1)
            if (len(s[idx:]) > 1) and (s[idx:idx+2] in poss_values2):
                r += dp_fn(idx+2)

            memo[idx] = r
            return r

        return dp_fn(0)