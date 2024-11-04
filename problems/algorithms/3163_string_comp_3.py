class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 0:
            return ""
        comp = ""
        prev = word[0]
        cpt = 0
        while len(word) > 0:
            while (cpt < 9) and (len(word) > 0) and (word[0] == prev):
                cpt += 1
                word = word[1:]
            comp += str(cpt) + prev
            cpt = 0
            prev = word[0] if len(word) > 0 else None
        return comp