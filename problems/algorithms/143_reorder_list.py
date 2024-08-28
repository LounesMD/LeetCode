from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        buffer = list()
        p0 = head 
        while p0 is not None:
            buffer.append(p0)
            p0 = p0.next

        nv_list = buffer[0]
        tail = None 
        for i in range(len(buffer) // 2):
            buffer[i].next=buffer[-1-i]
            buffer[i].next.next=buffer[i+1]
            tail=buffer[i].next.next
            
        if tail: 
            tail.next = None

        head = nv_list




sol = Solution()
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
res = sol.reorderList(l)
while res:
    print("res: ", res.val)
    res = res.next
