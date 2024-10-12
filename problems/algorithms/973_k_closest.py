import math
from typing import List

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        """
        Complexity: O(n*log(k))
        """
        distances = []
        
        for point in points:
            x, y = point[0], point[1]
            dist = x**2 + y**2
            if len(distances) == k:
                heapq.heappushpop(distances, (-dist, [x, y]))
            else:
                heapq.heappush(distances, (-dist, [x, y]))
                
        return [elt[1] for elt in distances]


    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Complexity: O(n*k)
        """
        def insert(dist, point, distances):
            left = 0 
            right = len(distances)
            while left < right:
                mid = left + (right - left) // 2
                if dist == distances[mid][0]:
                    return distances[:mid] + [(dist, point)] + distances[mid:]
                elif dist < distances[mid][0]:
                    right = mid 
                else: # dist > distances[mid]
                    left = mid + 1 

            return distances[:left] + [(dist, point)] + distances[left:]


        distances = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            distances = insert(dist, point, distances)
            if len(distances) > k:
                distances.pop()

        return [elt[1] for elt in distances[:k]]
    

    
    def kClosest_0(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Complexity: O(n*log(n))
        """
        distances = []

        for point in points:
            distances.append([math.sqrt(point[0]**2 + point[1]**2), point])

        distances = sorted(distances, key = lambda x : x[0])

        return [elt[1] for elt in distances][:k]
        

sol = Solution()
points = [[1,3],[-2,2]]
k = 1 
print(sol.kClosest(points, k))