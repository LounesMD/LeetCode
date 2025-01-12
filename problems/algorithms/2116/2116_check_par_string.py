class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if (n%2 == 1):
            return False
        left = 0
        v = 0

        for i in range(n):
            if locked[i] == "0":
                v += 1
            elif s[i] == "(":
                left += 1
            elif s[i] == ")":
                if left > 0:
                    left -= 1 
                elif v > 0:
                    v -= 1 
                else:
                    return False

        res = 0 
        for i in range(n-1, -1, -1):
            if locked[i] == "0":
                res -= 1
                v -= 1
            elif s[i] == "(":
                res += 1 
                left -= 1
            elif s[i] == ")":
                res -= 1
            if res > 0:
                return False
            if left == 0 and res == 0:
                break
        
        return left <= 0