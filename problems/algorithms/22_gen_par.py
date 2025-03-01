class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ress = []

        def rec(left,right,res):
            if (left + right) == 0:
                ress.append(res)
                return None
            if left > 0:
                rec(left - 1, right, res + '(')
            if right > left:
                rec(left, right - 1, res + ')')
        rec(n,n,'')
        return ress