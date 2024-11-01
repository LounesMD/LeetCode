class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        cpt = 1

        for letter in s[1:]:
            if letter == res[-1]:
                cpt += 1 
                if cpt < 3:
                    res += letter

            else:
                cpt = 1
                res += letter
        return res 

    def makeFancyString_0(self, s: str) -> str:
        i = 0 
        length = len(s)

        while i + 3 <= length:
            if s[i] == s[i+1] and s[i] == s[i+2]:
                s = s[:i] + s[i+1:]   
                length -= 1    
                i -= 1  
            i += 1 
        return s
        