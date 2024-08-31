class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cpt = 0
        for i in range(1, n + 1):
            if n %  i == 0:
                cpt += 1 
                if cpt == k:
                    return i
        return - 1 
    

sol = Solution()
n, k = 12, 3
print("res: ", sol.kthFactor(n, k))