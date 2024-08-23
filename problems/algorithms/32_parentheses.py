class Solution:
    def longestValidParentheses(self, s: str) -> int:
        op, cl = 0, 0
        max_len = 0

        for char in s:
            if char == '(':
                op += 1
            else:
                cl += 1
            if op == cl:
                max_len = max(max_len, 2 * op)
            elif cl > op: # more closed than opened, doesn't work
                op = cl = 0

        # Then from end to start if extra ")" at the beginning 
        op = cl = 0
        for char in s[::-1]:
            if char == '(':
                op += 1
            else:
                cl += 1
            if op == cl:
                max_len = max(max_len, 2 * op)
            elif op > cl:
                op = cl = 0

        return max_len


sol = Solution()
s = "()(()"
print("res: ", sol.longestValidParentheses(s))