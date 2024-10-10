from typing import List


class Solution:
    def insert0(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Complexity: O(nlog(n)) from the sort 
        """
        nv_list = []
        for interval in intervals:
            if newInterval[0] <= interval[0] <= newInterval[1] or newInterval[0] <= interval[1] <= newInterval[1]:                
                newInterval = [
                    min(newInterval[0] , interval[0]),
                    max(newInterval[1] , interval[1]),
                    ]
            elif interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1]:                
                newInterval = [
                    min(newInterval[0] , interval[0]),
                    max(newInterval[1] , interval[1]),
                    ]
            else:
                nv_list.append(interval)

        nv_list.append(newInterval)
        nv_list.sort(key=lambda x: x[0])
        return nv_list

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Complexity: O(n)
        """
        nv_list = []
        cpt = 0
        while cpt < len(intervals) and intervals[cpt][1] < newInterval[0]:
            nv_list.append(intervals[cpt])
            cpt += 1         

        while cpt < len(intervals) and intervals[cpt][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0] , intervals[cpt][0]),
                max(newInterval[1] , intervals[cpt][1]),
                ]
            cpt += 1 
        nv_list.append(newInterval)

        while cpt < len(intervals):
            nv_list.append(intervals[cpt])
            cpt += 1         

        return nv_list

sol = Solution()
intervals = [[1,5]]
newInterval = [2,3]
print(sol.insert(intervals, newInterval))