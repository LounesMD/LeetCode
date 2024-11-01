from typing import List 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [elt for elt in map[digits[0]]]

        for digit in digits[1:]:
            r = []
            for letter in map[digit]:
                for elt in res:
                    r.append(elt + letter)
            res = r
            r = []
        return res