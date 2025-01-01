class Solution:
    def maxScore(self, s: str) -> int:        
        #TODO: The loops could be mutualized such that we would not need additional space 
        res = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == "0":
                res[i] = res[i-1] + 1
            else:
                res[i] = res[i-1]

        nv_res = [0 for _ in range(len(s)+1)]
        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                nv_res[i] = nv_res[i+1] + 1
            else:
                nv_res[i] = nv_res[i+1]
        
                
        for i in range(len(res)-1):
            res[i] = res[i] + nv_res[i+1]

        return max(res[:-1])