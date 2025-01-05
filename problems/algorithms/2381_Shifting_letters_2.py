from typing import List 

class Solution:
    
    def shift_char(self, char, x):
        return chr((ord(char) - ord('a') + x) % 26 + ord('a'))


    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        dec = [0] * len(s)

        for shift in shifts:
            r = -1 if (shift[2] == 0) else 1
            dec[shift[0]] += r
            if shift[1] + 1 < len(dec):
                dec[shift[1] + 1] -= r

        for i in range(1, len(dec)):
            dec[i] += dec[i - 1]

        res = ""
        for i in range(len(s)):
            res += self.shift_char(s[i],dec[i])
        return res