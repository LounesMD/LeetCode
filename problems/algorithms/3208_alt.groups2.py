class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        cpt = 1
        n = len(colors)
        for i in range(1,n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                cpt += 1
                if cpt == k:
                    cpt -= 1
                    res += 1
            else:
                cpt = 1
        return res