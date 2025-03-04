class Solution(object):
    def checkPowersOfThree(self, n):
        while n > 1:
            if (n%3) == 2: # 0 and 1 are fine 
                return False
            n /= 3
        return True

    def checkPowersOfThree_rec(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True

        if (n%3) == 0:
            return self.checkPowersOfThree(n/3)
        elif (n-1)%3 == 0:
            return self.checkPowersOfThree((n-1)/3)
        else:
            return False