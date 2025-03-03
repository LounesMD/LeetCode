class Solution(object):
    def pivotArray_n(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        prev = []
        eq = 0
        sup = []
        for elt in nums:
            if elt < pivot:
                prev.append(elt)
            elif elt == pivot:
                eq += 1 
            else:
                sup.append(elt)

        return prev + [pivot for _ in range(eq)] + sup