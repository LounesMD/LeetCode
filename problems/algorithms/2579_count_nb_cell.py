class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 + n*(n-1)*2

        # res = 0
        # for i in range(1,2*n,2):
        #     res += i
        # return 2 * res - (2 * n - 1)