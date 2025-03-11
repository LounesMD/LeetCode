class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r, res, n = 0, 0, 0, len(s)

        freq ={"a":0,"b":0,"c":0}

        while r < n:
            freq[s[r]] += 1
            while (freq["a"] > 0) and (freq["b"] > 0) and (freq["c"] > 0):
                res += n - r
                freq[s[l]] -= 1
                l += 1
            r += 1

        return res