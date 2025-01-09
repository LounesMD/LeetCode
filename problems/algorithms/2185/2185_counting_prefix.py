from typing import List 

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cpt = 0 
        for word in words:
            # cpt += self.is_prefix(pref,word)
            if word.startswith(pref):
                cpt += 1 
        return cpt

    def is_prefix(self, str1: str, str2: str):
        if len(str1) > len(str2):
            return 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return 0
        return 1 

