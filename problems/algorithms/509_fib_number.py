class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        r1, r2 = 0, 1

        for _ in range(2, n+1):
            r1, r2 = r2, r1+r2
        return r2
    
    def fib0(self, n: int) -> int:
        if n ==0:
            return 0
        if n == 1:
            return 1
        r1 = self.fib(n-1)
        r2 = self.fib(n-2)
        return r1 + r2