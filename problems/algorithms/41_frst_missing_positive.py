from typing import List 

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Complexity: O(n*log(n))
        TODO: check a solution using O(n)
        """
        nums.sort() 
        min = 1 
        for elt in nums:
            if min == elt:
                min += 1 
            elif elt > min:
                return min
        return min         


sol = Solution()
nums = [7,8,9,11,12]
print("res: ", sol.firstMissingPositive(nums))