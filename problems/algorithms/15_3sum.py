from typing import List 

class Solution:
    def naive_threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (i!=j) and (i != k) and (j != k) and (nums[i] + nums[j] + nums[k] == 0):
                        sol = [nums[i],nums[j],nums[k]]
                        sol.sort()
                        if sol not in res:
                            res.append(sol)
        return res 
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Complexity: O(n^2).
        """
        res = set()
        # List sorted so we can remove duplicates faster.
        nums.sort()
        for i in range(len(nums)):
            # If the two first elements are equal, we skip to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            target = 0 - nums[i]
            # Now we use the two_sum approach
            elements = dict()
            for j in range(i+1, len(nums)):
                target_2 = target - nums[j]
                if target_2 in elements:
                    res.add((target_2, nums[i], nums[j])) 
                elements[nums[j]] = None 
        return [list(triplet) for triplet in res]


nums = [-1,0,1,2,-1,-4]

s = Solution()
print("res: ", s.threeSum(nums))
