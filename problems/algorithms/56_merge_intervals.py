from typing import List 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Complexity: sort
        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        merged.append(intervals[0])
        for interval in intervals[1:]:            
            prev_merged = merged[-1]
            if interval[0] <= prev_merged[1]:
                prev_merged[1] = max(prev_merged[1], interval[1])
            else:
                merged.append(interval)
        return merged
    
sol = Solution()
intervals = [[1,3],[2,6],[8,10], [9,16],[15,18], [1,20]]
# intervals = [[1,4],[4,5]]
print("res: ", sol.merge(intervals))