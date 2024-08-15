class Solution:
    def reverse(self, x: int) -> int:
        """
        Complexity: O(n).        
        """
        sign = -1 if (x < 0) else 1 
        x = abs(x)
        val2 = 0
        while x != 0 and - 2**(31) <= (val2*10 + x % 10) <= 2**(31) - 1 :
            print("l: ", x)
            val2 = (val2 * 10) + (x % 10)
            x = x // 10
        if x != 0:
            val2 = 0
        return sign * val2
    


s = Solution()
l = -123
print("res: ", s.reverse(l))