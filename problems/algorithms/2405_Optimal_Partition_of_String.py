class Solution:
    def partitionString_0(self, s: str) -> int:
        """
        Complexity: O(n^2)
        """
        partition = []
        i = 0
        while i < len(s):
            letters = {s[i] : None}
            current_partition = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in letters: 
                    letters[s[j]] = None 
                    current_partition = s[i:j+1]
                else:
                    partition.append(current_partition)
                    i += (j - i)
                    break

            else:
                partition.append(current_partition)
                break

        return len(partition)
    
    def partitionString(self, s: str) -> int:
        """
        Complexity: O(n)
        """
        n = 0
        current_substring = s[0]
        for j in range(1, len(s)):
            if s[j] not in current_substring: 
                current_substring += s[j]
            else:
                n += 1 
                current_substring = s[j]
        return n + 1


s = "abacaba"
sol = Solution()
print(sol.partitionString(s))