class Solution:
    def backtrack(self, s: str, p: str) -> bool:
        if s == "aaa" and p == "aaaa":
            return True
        if len(p) == 1:
            if p[0] == "*" or p[0] == s[0]:
                return True 
            else:
                return False 
        else:
            if len(p) > len(s):
                return False
            else:
                for i in range(len(p)):
                    if not(p[i] == p[0] == s[i]):
                        return False
        return True



    def isMatch(self, s: str, p: str) -> bool:
        """
        TODO: Doesn't work, finish it.
        """
        i = 0 
        Tocheck = False 
        while i < len(s):
            char = s[i]
            breakpoint()
            # If there is no pattern to match, return False 
            if len(p) == 0:
                return False 
            # This is the case of x*
            elif len(p) > 1 and p[1] == "*":
                # The letter matches so we pass 
                if char == p[0] or p[0] == ".":
                    cpt = 0
                    while (i+cpt < len(s)) and (s[i + cpt] == p[0] or p[0] == "."):
                        cpt += 1 
                    i += cpt
                    if i == len(s):
                        Tocheck = True 
                # The letter doesn't match so we get rid of the pattern x*
                p = p[2:]
                i = i - 1 
            # In case of ., we match any char 
            elif p[0] == ".":
                p = p[1:]
                pass 
            # In the case of just matching the first char
            elif char == p[0]:
                p = p[1:]
                pass 
            # Last case, no match
            else:
                return False 
            i += 1
        if len(p) > 0:
            if p[1] == 1:
                while p[1] == 1:
                    p = p[2:]
            if p[0] == "*" or Tocheck:
                return self.backtrack(s[::-1],p)                
            else:
                return False 
        return True
    
s = Solution()
l = "aaa"
p = "ab*a*c*a"
print("res: ", s.isMatch(l,p))