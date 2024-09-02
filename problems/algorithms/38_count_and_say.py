class Solution:
    def RLE(self, s: str) -> str:
        if not s:
            return ""
        prev = s[0]
        cpt = 0
        res = ""
        for elt in s:
            if elt == prev:
                cpt += 1
            else:                
                res += str(cpt) + prev                
                prev = elt 
                cpt = 1 
        res += str(cpt) + prev                
        return res 
    
    def countAndSay(self, n: int) -> str:
        res = "1"
        cpt = 1
        while cpt < n:
            res = self.RLE(res)
            cpt += 1
        return res 


sol = Solution()
n = 4
print("res: ", sol.countAndSay(n))