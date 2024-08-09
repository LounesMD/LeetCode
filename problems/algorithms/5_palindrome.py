class Solution:
    def longestPalindrome_naive(self, s: str) -> str:
        """
        Naive approach: Parse all substrings an keep the longest one.
        Complexity: O(n^3)
        """
        all_substrings = dict()
        for i in range(len(s)+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    all_substrings[i-j] = s[j:i]
        return all_substrings[max(all_substrings)]


    def longestPalindrome(self, s: str) -> str:
        """
        This algo browse the full list, and for all characters it expands around it until it has check all possible palindrome.
        Complexity: O(n^2)
        """
        longest_pal = ""
        def expand_left_right(left: int, right: int) -> str:
            # We expand to the left or right until we reach one of the boundaries 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            # Check for odd palindromes
            palindrome_odd = expand_left_right(i, i)
            if len(palindrome_odd) > len(longest_pal):
                longest_pal = palindrome_odd

            # Check for even palindromes
            palindrome_even = expand_left_right(i, i + 1)
            if len(palindrome_even) > len(longest_pal):
                longest_pal = palindrome_even

        return longest_pal



s = Solution()
l = "opababao"
print("res: ",s.longestPalindrome(l))