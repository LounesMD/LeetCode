class Solution:
    def minChanges(self, s: str) -> int:
        res = 0 
        cpt = 0 
        while cpt < len(s) - 1:
            if s[cpt] != s[cpt + 1]:
                res += 1 
            cpt += 2
        return res 