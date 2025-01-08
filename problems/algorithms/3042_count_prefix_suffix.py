from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cpt = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) <= len(words[j]):
                    # Works better to use {starts/ends}with() instead of in self.isPrefixAndSuffix(str1, str2)
                    if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                        cpt += 1 
        return cpt