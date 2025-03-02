class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        res = []
        while i < n and j < m:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1

            else:
                if nums1[i][0] < nums2[j][0]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1

        while i < n:
            res.append(nums1[i])
            i += 1 

        while j < m:
            res.append(nums2[j])
            j += 1             

        return res