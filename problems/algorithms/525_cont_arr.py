class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        # 1: How to know if a subarray has the same number of 0 and 1
        # cpt +1 if the val is 1 and -1 if 0. cpt = 0 => same number
        arr = [0]
        best = 0
        d = {}
        i = 1
        for elt in nums:
            if elt == 1:
                arr.append(arr[-1] + 1)
            else:
                arr.append(arr[-1] - 1)
        
        # for i in range(1, len(arr)):

            if arr[i] == 0:
                best = max(best, i)
            
            elif arr[i] in d:
                best = max(best, i-d[arr[i]] )

            else:
                d[arr[i]] = i
            i += 1
        return best