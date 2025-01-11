class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        letters = [0] * 26

        for letter in s:
            letters[ord('a') - ord(letter)] += 1
        
        odd = 0
        for val in letters:
            if val % 2 == 1:
                odd += 1
        
        return odd <= k