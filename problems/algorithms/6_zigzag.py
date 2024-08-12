class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Complexity: O(n)
        """
        l = [[] for _ in range(numRows)]
        shift = 0
        l[0].append(s[0])
        for i in range(1, len(s)):
            if ((i + shift) % numRows) == 0 :
                shift += 1 
                l.reverse()
            l[(i + shift) % numRows].append(s[i])
        if shift % 2 == 1:
            l.reverse()
        return ''.join([char for sublist in l for char in sublist])

        

s = Solution()
l = "ABC"
print("res: ",s.convert(l, 2))