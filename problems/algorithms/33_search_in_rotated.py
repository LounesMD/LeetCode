from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r)//2
            if nums[middle] == target:
                return middle

            elif nums[middle] >= target:
                if nums[middle] > target >= nums[l]:
                    r = middle - 1
                else:
                    l = middle + 1
            else:
                if nums[middle] < target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1
        return - 1

#  [5,6,7,0,1,2,3,4]

    def search0(self, nums: List[int], target: int) -> int:
        # nums sorted 
        cpt = 0
        for elt in nums:
            if elt == target:
                return cpt
            cpt += 1 
        return -1