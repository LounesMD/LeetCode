from typing import List

class Solution:
    def count(self, w:str) -> list[int]:
        letters = [0] * 26
        for letter in w:
            letters[ord('a') - ord(letter)] += 1
        return letters

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Note A list of fixed size is faster than a dict.
        """

        letters = [0] * 26
        for w in words2:
            count_l = self.count(w)
            for i in range(26):
                letters[i] = max(letters[i], count_l[i])

        res = []
        for word in words1:
            count1 = self.count(word)
            for i in range(26):
                if count1[i] < letters[i]:
                    break
            else:
                res.append(word)
        return res 