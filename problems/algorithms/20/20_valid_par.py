class Solution:
    def isValid(self, s: str) -> bool:    
        res = []
        for elt in s:
            if elt in "{[(":
                res.append(elt)
            else:
                if (not res) or \
                    (elt == ")" and res[-1] != "(") or \
                    (elt == "}" and res[-1] != "{") or \
                    (elt == "]" and res[-1] != "["):
                    return False
                res.pop()
        return len(res)==0 