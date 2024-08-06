class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elements = dict()
        max_cpt = 0
        sol = 0
        for i, char in enumerate(s):
            if char in elements:
                max_cpt = max(max_cpt, elements[char] + 1)
            elements[char] = i
            sol = max(sol, i - max_cpt + 1)
        return sol

test_cases = [
    {"input": "abcabcbb",
     "output": 3},          # Example provided: "abc"
    {"input": "bbbbb", "output": 1},             # Repeating characters: "b"
    {"input": "pwwkew", "output": 3},            # "wke"
    {"input": "abcdef", "output": 6},            # All unique characters: "abcdef"
    {"input": "", "output": 0},                  # Empty string
    {"input": " ", "output": 1},                 # Single space
    {"input": "aab", "output": 2},               # "ab"
    {"input": "dvdf", "output": 3},              # "vdf"
    {"input": "anviaj", "output": 5},            # "nviaj"
    {"input": "abacabcbb", "output": 3},         # "bac" or "cab"
    {"input": "tmmzuxt", "output": 5},           # "mzuxt"
    {"input": "qrsvbspk", "output": 5},          # "rsvbp"
    {"input": "abcdefgabcdefg", "output": 7},    # "abcdefg"
    {"input": "abcabcbb", "output": 3},          # "abc"
    {"input": "abcdee", "output": 5},            # "abcde"
    {"input": "abccba", "output": 3},            # "abc" or "cba"
    {"input": "aabbccddeeffgghh", "output": 2},  # "ab", "bc", "cd", etc.
    {"input": "abcdefghijjklmnop", "output": 10},# "abcdefghijklmno"
    {"input": "abrkaabcdefghijjxxx", "output": 10},# "abcdefghij"
    {"input": "abcabcbb", "output": 3},# "abcdefghij"
]

s = Solution()
for val in test_cases:
    assert s.lengthOfLongestSubstring(val["input"]) == val["output"]