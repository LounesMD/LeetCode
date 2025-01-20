from typing import List 

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        pos = dict()
        n, m = len(mat), len(mat[0])
        r_count, l_count = [0]*n,[0]*m

        for i in range(n):
            for j in range(m):
                pos[mat[i][j]] = (i,j)

        for k in range(len(arr)):
            i,j = pos[arr[k]]
            r_count[i] += 1
            l_count[j] += 1
            if r_count[i] == m or l_count[j] == n:
                return k