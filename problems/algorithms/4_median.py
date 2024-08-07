from typing import List 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        This solution has a complexity of: O(n+m).
        TODO: A better solution using binary search
        """
        m = len(nums1) # Size of the first array: Costs m
        n = len(nums2) # Size of the first array: Costs n
        l3 = list()
        i = 0 
        j = 0 

        # Merge the two sorted arrays: Cost O(n + m)
        while i < m and j < n:
            if(nums1[i] <  nums2[j]):
                l3.append(nums1[i])
                i += 1 
            else:
                l3.append(nums2[j])
                j += 1 
        while i < m:
            l3.append(nums1[i])
            i += 1         
        while j < n:
            l3.append(nums2[j])
            j += 1                     
        
        # Depends if the 'n+m' is even or not.
        i1 = (n+m)//2
        return (l3[i1 - (1-((n+m) % 2))] + l3[i1])/2
    


nums1 = [1,2]
nums2 = [3,4]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
