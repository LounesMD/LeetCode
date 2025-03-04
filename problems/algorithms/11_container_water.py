class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height) - 1

        while i < j:
            res = max(res, (j - i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
    
    def maxArea_no(self, height):
        res = 0
        for i in range(len(height)):
            for j in range(len(height)):
                res = max(res, (i-j)*min(height[i], height[j]))

        return res 