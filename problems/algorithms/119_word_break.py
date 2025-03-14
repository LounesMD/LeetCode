from typing import List 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Step 1: recursion
        # Step 2: memoization
        memo = {}

        def dp_sol(idx):
            if s[idx:] in wordDict:
                return True
            
            if idx in memo:
                return memo[idx]
            
            res = False
            
            for elt in wordDict:
                if len(elt) < len(s[idx:]) and s[idx:idx+len(elt)] == elt:
                    res = res or dp_sol(idx+len(elt))

            memo[idx] = res
            return res
        
        return dp_sol(0)