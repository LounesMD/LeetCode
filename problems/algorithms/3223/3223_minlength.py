class Solution:
    def minimumLength(self, s: str) -> int:
        pos = [0] * 26
        for letter in s:
            pos[ord(letter) - ord('a')] += 1 

        cpt = 0
        for n in pos:
            if n == 0:
                continue
            elif n % 2 == 0:
                cpt += 2
            else:
                cpt += 1

        return cpt