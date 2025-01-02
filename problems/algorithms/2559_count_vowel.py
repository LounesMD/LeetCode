from typing import List 

class Solution:
    def is_vowel(self,c):
        return c=="a" or c=="e" or c=="i" or c=="o" or c=="u"

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = [0]
        for elt in words:
            if self.is_vowel(elt[0]) and self.is_vowel(elt[-1]):
                res.append(res[-1] + 1)
            else:
                res.append(res[-1])
        too_sum = []
        for elt in queries:
            too_sum.append( res[elt[1]+1] - res[elt[0]])
        return too_sum