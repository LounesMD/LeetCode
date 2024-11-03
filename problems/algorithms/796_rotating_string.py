class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        length = len(s)
        i = 0
        j = 0
        cpt = 0 
        while i < 2*length:

            if s[i%length] == goal[j]:
                cpt += 1
                j += 1
                if cpt == length:
                    return True 

            else:
                i -= cpt 
                cpt = 0
                j = 0

            i += 1
        return False
        

    def rotateString_(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if (s[i:] + s[:i]) == goal:
                return True

        return False 
