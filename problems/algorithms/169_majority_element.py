from typing import List 

class Solution:
    def majorityElement_0(self, nums: List[int]) -> int:
        """
        Works even if maj res != sorted(nums)[len(nums)/2]...
        """
        nums = sorted(nums)

        current_elt = [0,0]
        prev_max = [0,0]

        for elt in nums:
            if elt == current_elt[0]:
                current_elt[1] += 1
                if current_elt[1] > prev_max[1]:
                    prev_max =[current_elt[0], current_elt[1]]
                
            if elt != current_elt[0]:                
                current_elt = [elt, 1]

        if current_elt[1] > prev_max[1]:
            prev_max =[current_elt[0], current_elt[1]]
        
        return prev_max[0]
    
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]