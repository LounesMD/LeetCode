class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Complexity: O(log(x))
        """
        if x == 0:
            return x 
        
        left, right = 1, x 
        while left <= right:
            middle = left + (right - left) // 2
            if middle * middle > x:
                right = middle - 1
            elif middle * middle < x:
                left = middle + 1
            else:
                return middle 
        return right

    def mySqrt_2(self, x: int) -> int:
        interm = 1 
        while interm * interm <= x:
            interm *= 2
        interm /= 2 
        while interm * interm <= x:
            interm += 1
        return int(interm) - 1       


sol = Solution()
x = 750
print("res: ", sol.mySqrt(x))
