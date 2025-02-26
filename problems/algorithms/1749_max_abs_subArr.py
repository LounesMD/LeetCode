from typing import List 

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # O(n) solution using Kadane's algorithm
        best_sum_pos = float('-inf')
        curr_sum = 0
        for x in nums:
            curr_sum = max(x, curr_sum + x)
            best_sum_pos = max(best_sum_pos, curr_sum)
        
        best_sum_neg = float('inf')
        curr_sum = 0
        for x in nums:
            curr_sum = min(x, curr_sum + x)
            best_sum_neg = min(best_sum_neg, curr_sum)

        return max(abs(best_sum_neg), best_sum_pos)
    
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # n^2 solution
        n = len(nums)
        best = [0] * n
        best[0] = nums[0]
        for i in range(1, n):
            best[i] = nums[i] + best[i-1]
        best.insert(0,0)
        res = best[0]
        # TODO: move from n^2 to n^1 loop
        for i in range(1, n+1):
            for j in range(i):
                # print(res, abs(best[j] - best[i]))
                res = max(res, abs(best[j] - best[i]))
        return res
    


n =[-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9] # [-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8]

s = Solution()
print(s.maxAbsoluteSum(n))


n =[-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8]

print(s.maxAbsoluteSum(n))