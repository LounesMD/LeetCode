from typing import List 

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """check KPM alg."""
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if (words[i] in words[j]) and (i != j):
                    res.append(words[i])
                    break
        return res