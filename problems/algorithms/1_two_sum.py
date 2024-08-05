from typing import List
import math 

class Solution:

    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        """
        double parsing of the list. O(n^2)
        """
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if i != j:
                    if(nums[i] + nums[j] == target):
                        return [i,j]
                                
    def twoSum_dict(self, nums: List[int], target: int) -> List[int]:
        """
        We parse the list just once using a dictionary to store parsed elements.
        Complexity: O(n)
        """
        parsed_elements = dict()
        for i in range(len(nums)):
            new_target = target-nums[i]
            if new_target in parsed_elements:
                return [i,parsed_elements[new_target]]
            parsed_elements[nums[i]] = i

nums = [3,2,4]
target = 6
sol = Solution()
print(sol.twoSum_dict(nums=nums, target=target))