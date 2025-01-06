from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        cpt_l = 0
        cpt_r = 0
        m_l = 0
        m_r = 0

        for i in range(n):
            res[i] += m_l
            cpt_l += int(boxes[i])
            m_l += cpt_l

            j = n - 1 - i
            res[j] += m_r
            cpt_r += int(boxes[j])
            m_r += cpt_r

        return res