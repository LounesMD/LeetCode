class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """ leetcode base solution
        """
        letters = set(s)
        cpt = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            
            for k in range(i + 1, j):
                between.add(s[k])
            
            cpt += len(between)

        return cpt

    def countPalindromicSubsequence_n2(self, s: str) -> int:
        if len(s) < 3:
            return 0 

        left = {}
        right = {}

        for elt in s:
            left[elt] = 0
            right[elt] = 0

        left[s[0]] += 1
        for elt in s[1:]:
            right[elt] += 1

        cpt = 0
        elts = {}
        n = len(s)
        for char in s[1:n-1]:
            right[char] -= 1
            for elt in left:
                if (left[elt] > 0) and (right[elt] > 0) and ((elt+char+elt) not in elts):
                    cpt += 1
                    elts[elt+char+elt] = None
            left[char] += 1            
        return cpt 

    def countPalindromicSubsequence_n3(self, s: str) -> int:
        if len(s) < 3:
            return 0 
        cpt = 0 
        left = s[0]
        right = s[2:]
        n = len(s)
        elt = []
        for char in s[1:n-1]:
            for l in left:
                for r in right:
                    if l == r and (l+char+r not in elt):
                        cpt += 1
                        elt.append(l+char+r)
            left += char
            right = right[1:]
        return cpt