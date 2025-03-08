class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        arr = [[0]* (len(str2)+1) for _ in range(len(str1)+1)]

        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    arr[i][j] = arr[i-1][j-1] + 1
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        i, j = len(str1), len(str2)
        res = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif arr[i - 1][j] >= arr[i][j - 1]:
                i -= 1
            else:
                j -= 1
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1 

        return "".join(res[::-1])
    

sol = Solution()
str1 = "abac"
str2 = "cab"

res = sol.shortestCommonSupersequence(str1, str2)
breakpoint()