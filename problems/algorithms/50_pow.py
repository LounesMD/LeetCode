class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x,abs(n))
        elif x == 0:
            return 0 
        elif n == 0:
            return 1
        
        elif n == 1:
            return x
        elif n % 2 == 0:
            res = self.myPow(x, n // 2)
            return  res * res 
        elif n % 2 == 1:
            res = self.myPow(x, n // 2)
            return x * res * res 
        

s = Solution()
print("res: ", s.myPow(2.0, -2147483648))