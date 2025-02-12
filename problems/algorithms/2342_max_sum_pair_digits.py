from typing import List 

class Solution:
    def ssum(self, n):
        # return sum(int(digit) for digit in str(n))
        a, n = n%10, n//10
        while n != 0:
            a += n % 10 
            n //= 10
        return a

    def maximumSum(self, nums: List[int]) -> int:
        dup = [(self.ssum(elt), elt) for elt in nums]
        dup.sort()
        res = -1
        for i in range(len(dup) - 1):            
            if dup[i][0] == dup[i+1][0]:
                res = max(res, dup[i][1] + dup[i+1][1])
        return res